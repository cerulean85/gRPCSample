package net.kkennib.grpc;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.35.0)",
    comments = "Source: bee4.proto")
public final class Bee4ServiceGrpc {

  private Bee4ServiceGrpc() {}

  public static final String SERVICE_NAME = "Bee4Service";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<net.kkennib.grpc.EmptyParam,
      net.kkennib.grpc.NodeCondition> getAreYouHealthyMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "AreYouHealthy",
      requestType = net.kkennib.grpc.EmptyParam.class,
      responseType = net.kkennib.grpc.NodeCondition.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<net.kkennib.grpc.EmptyParam,
      net.kkennib.grpc.NodeCondition> getAreYouHealthyMethod() {
    io.grpc.MethodDescriptor<net.kkennib.grpc.EmptyParam, net.kkennib.grpc.NodeCondition> getAreYouHealthyMethod;
    if ((getAreYouHealthyMethod = Bee4ServiceGrpc.getAreYouHealthyMethod) == null) {
      synchronized (Bee4ServiceGrpc.class) {
        if ((getAreYouHealthyMethod = Bee4ServiceGrpc.getAreYouHealthyMethod) == null) {
          Bee4ServiceGrpc.getAreYouHealthyMethod = getAreYouHealthyMethod =
              io.grpc.MethodDescriptor.<net.kkennib.grpc.EmptyParam, net.kkennib.grpc.NodeCondition>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "AreYouHealthy"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  net.kkennib.grpc.EmptyParam.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  net.kkennib.grpc.NodeCondition.getDefaultInstance()))
              .setSchemaDescriptor(new Bee4ServiceMethodDescriptorSupplier("AreYouHealthy"))
              .build();
        }
      }
    }
    return getAreYouHealthyMethod;
  }

  private static volatile io.grpc.MethodDescriptor<net.kkennib.grpc.EmptyParam,
      net.kkennib.grpc.NodeCondition> getAreYouIdleMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "AreYouIdle",
      requestType = net.kkennib.grpc.EmptyParam.class,
      responseType = net.kkennib.grpc.NodeCondition.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<net.kkennib.grpc.EmptyParam,
      net.kkennib.grpc.NodeCondition> getAreYouIdleMethod() {
    io.grpc.MethodDescriptor<net.kkennib.grpc.EmptyParam, net.kkennib.grpc.NodeCondition> getAreYouIdleMethod;
    if ((getAreYouIdleMethod = Bee4ServiceGrpc.getAreYouIdleMethod) == null) {
      synchronized (Bee4ServiceGrpc.class) {
        if ((getAreYouIdleMethod = Bee4ServiceGrpc.getAreYouIdleMethod) == null) {
          Bee4ServiceGrpc.getAreYouIdleMethod = getAreYouIdleMethod =
              io.grpc.MethodDescriptor.<net.kkennib.grpc.EmptyParam, net.kkennib.grpc.NodeCondition>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "AreYouIdle"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  net.kkennib.grpc.EmptyParam.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  net.kkennib.grpc.NodeCondition.getDefaultInstance()))
              .setSchemaDescriptor(new Bee4ServiceMethodDescriptorSupplier("AreYouIdle"))
              .build();
        }
      }
    }
    return getAreYouIdleMethod;
  }

  private static volatile io.grpc.MethodDescriptor<net.kkennib.grpc.Feed,
      net.kkennib.grpc.Feed> getDeliverMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "Deliver",
      requestType = net.kkennib.grpc.Feed.class,
      responseType = net.kkennib.grpc.Feed.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<net.kkennib.grpc.Feed,
      net.kkennib.grpc.Feed> getDeliverMethod() {
    io.grpc.MethodDescriptor<net.kkennib.grpc.Feed, net.kkennib.grpc.Feed> getDeliverMethod;
    if ((getDeliverMethod = Bee4ServiceGrpc.getDeliverMethod) == null) {
      synchronized (Bee4ServiceGrpc.class) {
        if ((getDeliverMethod = Bee4ServiceGrpc.getDeliverMethod) == null) {
          Bee4ServiceGrpc.getDeliverMethod = getDeliverMethod =
              io.grpc.MethodDescriptor.<net.kkennib.grpc.Feed, net.kkennib.grpc.Feed>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "Deliver"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  net.kkennib.grpc.Feed.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  net.kkennib.grpc.Feed.getDefaultInstance()))
              .setSchemaDescriptor(new Bee4ServiceMethodDescriptorSupplier("Deliver"))
              .build();
        }
      }
    }
    return getDeliverMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static Bee4ServiceStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<Bee4ServiceStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<Bee4ServiceStub>() {
        @java.lang.Override
        public Bee4ServiceStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new Bee4ServiceStub(channel, callOptions);
        }
      };
    return Bee4ServiceStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static Bee4ServiceBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<Bee4ServiceBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<Bee4ServiceBlockingStub>() {
        @java.lang.Override
        public Bee4ServiceBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new Bee4ServiceBlockingStub(channel, callOptions);
        }
      };
    return Bee4ServiceBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static Bee4ServiceFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<Bee4ServiceFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<Bee4ServiceFutureStub>() {
        @java.lang.Override
        public Bee4ServiceFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new Bee4ServiceFutureStub(channel, callOptions);
        }
      };
    return Bee4ServiceFutureStub.newStub(factory, channel);
  }

  /**
   */
  public static abstract class Bee4ServiceImplBase implements io.grpc.BindableService {

    /**
     */
    public void areYouHealthy(net.kkennib.grpc.EmptyParam request,
        io.grpc.stub.StreamObserver<net.kkennib.grpc.NodeCondition> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getAreYouHealthyMethod(), responseObserver);
    }

    /**
     */
    public void areYouIdle(net.kkennib.grpc.EmptyParam request,
        io.grpc.stub.StreamObserver<net.kkennib.grpc.NodeCondition> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getAreYouIdleMethod(), responseObserver);
    }

    /**
     */
    public void deliver(net.kkennib.grpc.Feed request,
        io.grpc.stub.StreamObserver<net.kkennib.grpc.Feed> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getDeliverMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getAreYouHealthyMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                net.kkennib.grpc.EmptyParam,
                net.kkennib.grpc.NodeCondition>(
                  this, METHODID_ARE_YOU_HEALTHY)))
          .addMethod(
            getAreYouIdleMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                net.kkennib.grpc.EmptyParam,
                net.kkennib.grpc.NodeCondition>(
                  this, METHODID_ARE_YOU_IDLE)))
          .addMethod(
            getDeliverMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                net.kkennib.grpc.Feed,
                net.kkennib.grpc.Feed>(
                  this, METHODID_DELIVER)))
          .build();
    }
  }

  /**
   */
  public static final class Bee4ServiceStub extends io.grpc.stub.AbstractAsyncStub<Bee4ServiceStub> {
    private Bee4ServiceStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected Bee4ServiceStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new Bee4ServiceStub(channel, callOptions);
    }

    /**
     */
    public void areYouHealthy(net.kkennib.grpc.EmptyParam request,
        io.grpc.stub.StreamObserver<net.kkennib.grpc.NodeCondition> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getAreYouHealthyMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void areYouIdle(net.kkennib.grpc.EmptyParam request,
        io.grpc.stub.StreamObserver<net.kkennib.grpc.NodeCondition> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getAreYouIdleMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void deliver(net.kkennib.grpc.Feed request,
        io.grpc.stub.StreamObserver<net.kkennib.grpc.Feed> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getDeliverMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class Bee4ServiceBlockingStub extends io.grpc.stub.AbstractBlockingStub<Bee4ServiceBlockingStub> {
    private Bee4ServiceBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected Bee4ServiceBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new Bee4ServiceBlockingStub(channel, callOptions);
    }

    /**
     */
    public net.kkennib.grpc.NodeCondition areYouHealthy(net.kkennib.grpc.EmptyParam request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getAreYouHealthyMethod(), getCallOptions(), request);
    }

    /**
     */
    public net.kkennib.grpc.NodeCondition areYouIdle(net.kkennib.grpc.EmptyParam request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getAreYouIdleMethod(), getCallOptions(), request);
    }

    /**
     */
    public net.kkennib.grpc.Feed deliver(net.kkennib.grpc.Feed request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getDeliverMethod(), getCallOptions(), request);
    }
  }

  /**
   */
  public static final class Bee4ServiceFutureStub extends io.grpc.stub.AbstractFutureStub<Bee4ServiceFutureStub> {
    private Bee4ServiceFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected Bee4ServiceFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new Bee4ServiceFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<net.kkennib.grpc.NodeCondition> areYouHealthy(
        net.kkennib.grpc.EmptyParam request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getAreYouHealthyMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<net.kkennib.grpc.NodeCondition> areYouIdle(
        net.kkennib.grpc.EmptyParam request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getAreYouIdleMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<net.kkennib.grpc.Feed> deliver(
        net.kkennib.grpc.Feed request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getDeliverMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_ARE_YOU_HEALTHY = 0;
  private static final int METHODID_ARE_YOU_IDLE = 1;
  private static final int METHODID_DELIVER = 2;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final Bee4ServiceImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(Bee4ServiceImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_ARE_YOU_HEALTHY:
          serviceImpl.areYouHealthy((net.kkennib.grpc.EmptyParam) request,
              (io.grpc.stub.StreamObserver<net.kkennib.grpc.NodeCondition>) responseObserver);
          break;
        case METHODID_ARE_YOU_IDLE:
          serviceImpl.areYouIdle((net.kkennib.grpc.EmptyParam) request,
              (io.grpc.stub.StreamObserver<net.kkennib.grpc.NodeCondition>) responseObserver);
          break;
        case METHODID_DELIVER:
          serviceImpl.deliver((net.kkennib.grpc.Feed) request,
              (io.grpc.stub.StreamObserver<net.kkennib.grpc.Feed>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class Bee4ServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    Bee4ServiceBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return net.kkennib.grpc.Bee4Proto.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("Bee4Service");
    }
  }

  private static final class Bee4ServiceFileDescriptorSupplier
      extends Bee4ServiceBaseDescriptorSupplier {
    Bee4ServiceFileDescriptorSupplier() {}
  }

  private static final class Bee4ServiceMethodDescriptorSupplier
      extends Bee4ServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    Bee4ServiceMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (Bee4ServiceGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new Bee4ServiceFileDescriptorSupplier())
              .addMethod(getAreYouHealthyMethod())
              .addMethod(getAreYouIdleMethod())
              .addMethod(getDeliverMethod())
              .build();
        }
      }
    }
    return result;
  }
}
