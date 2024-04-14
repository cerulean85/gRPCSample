package net.kkennib.grpc;

import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class GrpcClientController {

    @Autowired
    private final GrpcClientService grpcClientService;

    @GetMapping("/are_you_healthy")
    public boolean areYouHealthy() {
        return grpcClientService.areYouHealthy();
    }
}

