import kfp.dsl as dsl
from kubernetes import client as k8s_client


def TrainOp(vop):
    return dsl.ContainerOp(
        name="training pipeline",
        image="10.161.31.82:5000/phm:0.1-enas-train",

        command = [
            "sh", "run_train_container.sh"
        ],
        pvolumes={"src/data": vop},
    ).add_pod_label("app", "enas-application")

def VolumnOp():
    return dsl.PipelineVolume(
        pvc="phm-volume"
    )

@dsl.pipeline(
    name='enas_pipeline',
    description='ENAS pipeline'
)
def enas_pipeline(
):
    print('enas_pipeline')

    vop = VolumnOp()
    dsl.get_pipeline_conf().set_image_pull_secrets([k8s_client.V1LocalObjectReference(name='regcredidc')])
    train_and_eval = TrainOp(vop)


if __name__ == '__main__':
    import kfp.compiler as compiler
    # compiler.Compiler().compile(gnn_pipeline, __file__ + '.tar.gz')
    compiler.Compiler().compile(enas_pipeline, __file__ + '.yaml')

