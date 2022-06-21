import kfp.dsl as dsl
from kubernetes import client as k8s_client

def TrainOp(train_data, val_data, vop):
    return dsl.ContainerOp(
        name="training pipeline",
        image="10.161.31.82:5000/phm:0.1-enas-train",

        command = [
            "sh", "run_train_container.sh"
        ],
        arguments=[
            train_data, val_data
        ],
        output_artifact_paths={
            'mlpipeline-metrics': 'data/mlpipeline-metrics.json'
        },
        pvolumes={"src/data": vop},
    ).add_pod_label("app", "enas-application")

def ServeOp(trainop):
    return dsl.ContainerOp(
        name="serve pipeline",
        image="10.161.31.82:5000/phm:0.1-enas-serve",
        command = [
            "sh", "run_serve_container.sh"
        ],
        pvolumes={"src/data": trainop.pvolume},
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


    train_and_eval = TrainOp(
        vop
    )


    serve = ServeOp(train_and_eval)

    serve.after(train_and_eval)


if __name__ == '__main__':
    import kfp.compiler as compiler
    # compiler.Compiler().compile(enas_pipeline, __file__ + '.tar.gz')
    compiler.Compiler().compile(enas_pipeline, __file__ + '.yaml')