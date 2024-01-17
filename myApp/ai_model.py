def aimodel(img):
    PAT = '9529c88f474941618e4b6afa89a124f7'

    USER_ID = 'sin_chan66'
    APP_ID = 'Detection_Apparel'

    MODEL_ID = '001-Run-03'
    MODEL_VERSION_ID = '505326c150bb4618b7877b844f22bd10'
    IMAGE_URL = img
    from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
    from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
    from clarifai_grpc.grpc.api.status import status_code_pb2

    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + PAT),)

    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,  # The userDataObject is created in the overview and is required when using a PAT
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,  # This is optional. Defaults to the latest model version
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            url=IMAGE_URL
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    # Since we have one input, one output will exist here
    output = post_model_outputs_response.outputs[0]

    # print("Predicted concepts:")
    for concept in output.data.concepts:
        accuracy=concept.value
        if round(accuracy)==1:
            op1=str(f"This is a {concept.name}.\nAccuracy= {concept.value*100:.2f} %")
            return op1
        # print("%s %.2f" % (concept.name, concept.value))

    # Uncomment this line to print the full Response JSON
    # print(output)
# aimodel("https://static.lefties.com/9/photos2/2024/V/0/2/p/5323/529/400/5323529400_2_1_1.jpg?t=1695203474965")