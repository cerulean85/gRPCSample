package net.kkennib.grpc;

import io.grpc.StatusRuntimeException;
import net.devh.boot.grpc.client.inject.GrpcClient;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.util.Objects;

@Service
public class GrpcClientService {

    @GrpcClient("bee4")
    private Bee4ServiceGrpc.Bee4ServiceBlockingStub bee4Stub;

    @Value("${run.type}")
    private String runType;

    public void test()
    {
        System.out.println(runType);
        System.out.println(runType);
        System.out.println(runType);
        System.out.println(runType);
        System.out.println(runType);
    }

    public boolean areYouHealthy() {
        if (Objects.equals(runType, "active-active"))
            return true;

        try{
            NodeCondition response = this.bee4Stub.areYouHealthy(EmptyParam.newBuilder().build());
            boolean isHealthy = response.getHealthy();
            return isHealthy;
        } catch (StatusRuntimeException e) {
            return false;
        }
    }
}
