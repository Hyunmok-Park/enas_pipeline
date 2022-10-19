import kfp.dsl as dsl
from kubernetes import client as k8s_client

def TrainOp(vop):
    return dsl.ContainerOp(
        name="training pipeline",
        image="****:5000/phm:0.1-enas-train",

        command = [
            "sh", "run_train_container.sh"
        ],

        pvolumes={"src/data": vop},
    ).add_pod_label("app", "enas-application")

def ReTrainOp(trainop):
    return dsl.ContainerOp(
        name="retraining pipeline",
        image="****:5000/phm:0.1-enas-retrain",

        command = [
            "sh", "run_retrain_container.sh"
        ],

        pvolumes={"src/data": trainop.pvolume},
    ).add_pod_label("app", "enas-application")

def ServeOp(retrainop):
    return dsl.ContainerOp(
        name="serve pipeline",
        image="****:5000/phm:0.1-enas-serve",
        command = [
            "sh", "run_serve_container.sh"
        ],
        pvolumes={"src/data": retrainop.pvolume},
    ).add_pod_label("app", "enas-application")

def VolumnOp():
    return dsl.PipelineVolume(
        pvc="phm-volume"
    )

@dsl.pipeline(
    name='enas_pipeline',
    description='Probabilistic inference with graph neural network'
)
def enas_pipeline(
):
    print('enas_pipeline')

    vop = VolumnOp()

    dsl.get_pipeline_conf().set_image_pull_secrets([k8s_client.V1LocalObjectReference(name='regcredidc')])

    train_and_eval = TrainOp(vop)

    retrain = ReTrainOp(train_and_eval)
    retrain.after(train_and_eval)

    serve = ServeOp(retrain)
    serve.after(train_and_eval)


if __name__ == '__main__':
    import kfp.compiler as compiler
    # compiler.Compiler().compile(enas_pipeline, __file__ + '.tar.gz')
    compiler.Compiler().compile(enas_pipeline, __file__ + '.yaml')