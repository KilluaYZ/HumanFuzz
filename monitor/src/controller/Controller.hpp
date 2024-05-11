#ifndef CONTROLLER_HPP
#define CONTROLLER_HPP

#include "oatpp/web/server/HttpConnectionHandler.hpp"
#include "oatpp/network/Server.hpp"
#include "oatpp/network/tcp/server/ConnectionProvider.hpp"
#include "../dto/MsgDto.hpp"
#include "../FuzzerManager/FuzzerManager.hpp"
#include <iostream>
#include <sstream>
#include <string>
#include "../utils/mjson.hpp"

class PauseFuzzHandler : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    PauseFuzzHandler(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            this->m_fuzzerManager->get_fuzzer(fuzzer_id)->pause();
            message->statusCode = 200;
            message->message = "pause success";
            OATPP_LOGI("AFL_MONITOR", "visiting /pause with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("pause failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /pause with code %d", 500);
        }

        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};

class ResumeFuzzHandler : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    ResumeFuzzHandler(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            this->m_fuzzerManager->get_fuzzer(fuzzer_id)->resume();
            message->statusCode = 200;
            message->message = "resume success";
            OATPP_LOGI("AFL_MONITOR", "visiting /resume with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("resume failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /resume with code %d", 500);
        }

        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};

class StopFuzzHandler : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    StopFuzzHandler(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            this->m_fuzzerManager->get_fuzzer(fuzzer_id)->stop();
            message->statusCode = 200;
            message->message = "stop success";
            OATPP_LOGI("AFL_MONITOR", "visiting /stop with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("stop failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /stop with code %d", 500);
        }

        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};

class SkipCurCaseHandler : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    SkipCurCaseHandler(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            this->m_fuzzerManager->get_fuzzer(fuzzer_id)->skip_cur_case();
            message->statusCode = 200;
            message->message = "skip cur case success";
            OATPP_LOGI("AFL_MONITOR", "visiting /skip with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("skip cur case failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /skip with code %d", 500);
        }

        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};

class AddFuzzerHandler : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    AddFuzzerHandler(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            std::string shared_file_path = mj.getString("shared_file_path");
            std::cout<<"shared_file_path = "<<shared_file_path<<std::endl;
            auto fuzzer = m_fuzzerManager->add_fuzzer(fuzzer_id, shared_file_path);
            fuzzer->connect();
            message->statusCode = 200;
            message->message = "add success";
            OATPP_LOGI("AFL_MONITOR", "visiting /add with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("add failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /add with code %d", 500);
        }

        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};

class ReadAllHandler : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    ReadAllHandler(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            auto fuzzer = this->m_fuzzerManager->get_fuzzer(fuzzer_id);
            mJson msgJson =  fuzzer->to_json();
            message->statusCode = 200;
            message->message = msgJson.dumps();
            OATPP_LOGI("AFL_MONITOR", "visiting /read/all with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("/read/all failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /read/all with code %d", 500);
        }
        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};

class ReadQueueHandler : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    ReadQueueHandler(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            auto fuzzer = this->m_fuzzerManager->get_fuzzer(fuzzer_id);
            mJson msgJson =  fuzzer->read_queue();
            message->statusCode = 200;
            message->message = msgJson.dumps();
            OATPP_LOGI("AFL_MONITOR", "visiting /read/queue with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("/read/queue failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /read/queue with code %d", 500);
        }
        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};

class ReadQueueCurHandler : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    ReadQueueCurHandler(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            auto fuzzer = this->m_fuzzerManager->get_fuzzer(fuzzer_id);
            mJson msgJson =  fuzzer->read_queue_cur();
            message->statusCode = 200;
            message->message = msgJson.dumps();
            OATPP_LOGI("AFL_MONITOR", "visiting /read/cur with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("/read/cur failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /read/cur with code %d", 500);
        }
        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};

class WriteQueueHandler : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    WriteQueueHandler(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            mJson queue = mj.getJson("queue");
            auto fuzzer = this->m_fuzzerManager->get_fuzzer(fuzzer_id);
            fuzzer->write_queue(queue);
            message->statusCode = 200;
            message->message = "write queue success";
            OATPP_LOGI("AFL_MONITOR", "visiting /write/queue with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("/write/queue failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /write/queue with code %d", 500);
        }
        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};

class WriteQueueCurHandler : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    WriteQueueCurHandler(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            mJson queue_cur = mj.getJson("queue_cur");
            auto fuzzer = this->m_fuzzerManager->get_fuzzer(fuzzer_id);
            fuzzer->write_queue_cur(queue_cur);
            message->statusCode = 200;
            message->message = "write queue_cur success";
            OATPP_LOGI("AFL_MONITOR", "visiting /write/cur with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("/write/cur failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /write/cur with code %d", 500);
        }
        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};


class ReadFuzzStat : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    ReadFuzzStat(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            auto fuzzer = this->m_fuzzerManager->get_fuzzer(fuzzer_id);
            mJson msgJson =  fuzzer->read_fuzz_stat();
            message->statusCode = 200;
            message->message = msgJson.dumps();
            OATPP_LOGI("AFL_MONITOR", "visiting /read/stat with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("/read/stat failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /read/stat with code %d", 500);
        }
        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};

class WriteQueueByIdHandler : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    WriteQueueByIdHandler(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            mJson modify_queue_entry = mj.getJson("modify_queue_entry");
            int modify_queue_entry_idx = mj.getInt("modify_queue_entry_idx");
            auto fuzzer = this->m_fuzzerManager->get_fuzzer(fuzzer_id);
            fuzzer->write_queue_by_id(modify_queue_entry_idx, modify_queue_entry);
            message->statusCode = 200;
            message->message = "write queue by id success";
            OATPP_LOGI("AFL_MONITOR", "visiting /write/byid with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("/write/byid failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /write/byid with code %d", 500);
        }
        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};

class FuzzTargetCaseByIdHandler : public oatpp::web::server::HttpRequestHandler {
private:
    std::shared_ptr<oatpp::data::mapping::ObjectMapper> m_objectMapper;
    FuzzerManager *m_fuzzerManager;

public:
    FuzzTargetCaseByIdHandler(const std::shared_ptr<oatpp::data::mapping::ObjectMapper>& objectMapper, FuzzerManager* fuzzer_manager) : m_objectMapper(objectMapper) {
        m_fuzzerManager = fuzzer_manager;
    }

    std::shared_ptr<OutgoingResponse> handle(const std::shared_ptr<IncomingRequest>& request) override {
        auto message = MessageDto::createShared();
        try{
            auto request_body_str = request->readBodyToString();
            mJson mj;
            mj.loads(request_body_str);
            std::string fuzzer_id = mj.getString("fuzzer_id");
            int target_case_id = mj.getInt("target_queue_entry_idx");
            auto fuzzer = this->m_fuzzerManager->get_fuzzer(fuzzer_id);
            fuzzer->fuzz_target_case_by_id(target_case_id);
            message->statusCode = 200;
            message->message = "fuzz target case success";
            OATPP_LOGI("AFL_MONITOR", "visiting /fuzzbyid with code %d", 200);
        }catch(std::exception& e){
            std::cerr<<e.what()<<std::endl;
            message->statusCode = 500;
            message->message = std::string("fuzz target case failed: ")+std::string(e.what());
            OATPP_LOGE("AFL_MONITOR", "visiting /fuzzbyid with code %d", 500);
        }
        return ResponseFactory::createResponse(Status::CODE_200, message, m_objectMapper);
    }
};
#endif 