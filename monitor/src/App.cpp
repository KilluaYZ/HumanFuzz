#include "controller/TestController.hpp"

#include "oatpp/web/server/HttpConnectionHandler.hpp"

#include "oatpp/network/Server.hpp"
#include "oatpp/network/tcp/server/ConnectionProvider.hpp"
#include "controller/Controller.hpp"
#include "FuzzerManager/FuzzerManager.hpp"

void run(){
    auto objectMapper = oatpp::parser::json::mapping::ObjectMapper::createShared();
    auto router = oatpp::web::server::HttpRouter::createShared();
    auto fuzzer_manager = new FuzzerManager();
    router->route("GET", "/hello", std::make_shared<TestHandler>(objectMapper));
    router->route("POST", "/add", std::make_shared<AddFuzzerHandler>(objectMapper, fuzzer_manager));
    router->route("POST", "/pause", std::make_shared<PauseFuzzHandler>(objectMapper, fuzzer_manager));
    router->route("POST", "/skip", std::make_shared<SkipCurCaseHandler>(objectMapper, fuzzer_manager));
    router->route("POST", "/stop", std::make_shared<StopFuzzHandler>(objectMapper, fuzzer_manager));
    router->route("POST", "/resume", std::make_shared<ResumeFuzzHandler>(objectMapper, fuzzer_manager));
    router->route("POST", "/read/all", std::make_shared<ReadAllHandler>(objectMapper, fuzzer_manager));
    router->route("POST", "/read/queue", std::make_shared<ReadQueueHandler>(objectMapper, fuzzer_manager));
    router->route("POST", "/read/cur", std::make_shared<ReadQueueCurHandler>(objectMapper, fuzzer_manager));
    router->route("POST", "/write/queue", std::make_shared<WriteQueueHandler>(objectMapper, fuzzer_manager));
    router->route("POST", "/write/cur", std::make_shared<WriteQueueCurHandler>(objectMapper, fuzzer_manager));
    router->route("POST", "/read/stat", std::make_shared<ReadFuzzStat>(objectMapper, fuzzer_manager));
    router->route("POST", "/write/byid", std::make_shared<WriteQueueByIdHandler>(objectMapper, fuzzer_manager));
    router->route("POST", "/fuzzbyid", std::make_shared<FuzzTargetCaseByIdHandler>(objectMapper, fuzzer_manager));


    /* Create HTTP connection handler with router */
    auto connectionHandler = oatpp::web::server::HttpConnectionHandler::createShared(router);

    /* Create TCP connection provider */
    auto connectionProvider = oatpp::network::tcp::server::ConnectionProvider::createShared({"localhost", 8000, oatpp::network::Address::IP_4});

    /* Create server which takes provided TCP connections and passes them to HTTP connection handler */
    oatpp::network::Server server(connectionProvider, connectionHandler);

    /* Priny info about server port */
    OATPP_LOGI("AFL_MONITOR", "Server running on port %s", connectionProvider->getProperty("port").getData());

    /* Run server */
    server.run();
}

int main() {
    /* Init oatpp Environment */
    oatpp::base::Environment::init();
    /* Run App */
    run();

    /* Destroy oatpp Environment */
    oatpp::base::Environment::destroy();

    return 0;
}