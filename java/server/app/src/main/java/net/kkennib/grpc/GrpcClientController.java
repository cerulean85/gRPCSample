package net.kkennib.grpc;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

@Controller
public class GrpcClientController {
    @Autowired
    public GrpcClientService grpcClientService;

    public String sendMessage(String message) {
        return grpcClientService.sendMessage(message);
    }
}
