package net.kkennib.grpc;
import io.grpc.stub.StreamObserver;
import net.devh.boot.grpc.server.service.GrpcService;

@GrpcService
public class GrpcServerService extends Bee4ServiceGrpc.Bee4ServiceImplBase {
    @Override
    public void areYouHealthy(EmptyParam request, StreamObserver<NodeCondition> responseObserver) {
        NodeCondition cond = NodeCondition.newBuilder().setHealthy(true).build();
        responseObserver.onNext(cond);
        responseObserver.onCompleted();
    }
}



