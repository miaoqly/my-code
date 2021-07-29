# File ：login_test.py
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseMubuLogin(HttpRunner):
    config = (
        Config("testcase description")
        .variables(**{
            "phone":"13554170217",
            "password":"919299",
            "host":"mubu.com"
        })
        .base_url("https://$host")
        .export("JwtToken","userId")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("/")
                .get("/")
                .with_headers(
                **{
                    "cache-control": "max-age=0",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://mubu.com/app",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_cookies(
                **{
                    "language": "en-US",
                    "country": "US",
                    "reg_prepareId": "177d17d8afa-177d17d8ae9-4b67-a971-98f46b2df272",
                    "reg_focusId": "54e33e80-b883-4b67-a971-177d17d902e",
                    "SLARDAR_WEB_ID": "7d4226e8-f211-4b9e-954b-4abc4c306cb5",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login")
                .get("/login")
                .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_cookies(
                **{
                    "language": "en-US",
                    "country": "US",
                    "reg_prepareId": "177d17d8afa-177d17d8ae9-4b67-a971-98f46b2df272",
                    "reg_focusId": "54e33e80-b883-4b67-a971-177d17d902e",
                    "SLARDAR_WEB_ID": "afbbfb78-d1ed-456b-872f-cc37ac5c3848",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login/password")
                .get("/login/password")
                .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://mubu.com/login",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_cookies(
                **{
                    "language": "en-US",
                    "country": "US",
                    "SLARDAR_WEB_ID": "a52042eb-1924-4b9e-b28d-fbb68c53f738",
                    "reg_prepareId": "177d1973926-177d1973676-4ab6-9c11-430341609505",
                    "reg_focusId": "9e853826-cbb4-4ab6-9c11-177d1973d24",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/api/login/submit")
                .with_variables(**{
                "remember":"true",
                "timestamp":"${get_timestamp()}"
            })
                .post("/api/login/submit")
                .with_headers(
                **{
                    "content-length": "47",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "x-requested-with": "XMLHttpRequest",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/login/password",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_cookies(
                **{
                    "language": "en-US",
                    "country": "US",
                    "reg_prepareId": "177d1973926-177d1973676-4ab6-9c11-430341609505",
                    "reg_focusId": "9e853826-cbb4-4ab6-9c11-177d1973d24",
                    "SLARDAR_WEB_ID": "d07bcb26-1fe3-447a-95c5-bb7a30c90c80",
                }
            )
                .with_data(
                {
                    "phone": "$phone",
                    "password": "$password",
                    "remember": "$remember",
                    "token":"${gen_token($phone,$password,$timestamp)}"
                }
            )
                .teardown_hook("${sleep(2)}")
                .extract()
                .with_jmespath('cookies."Jwt-Token"',"JwtToken")
                .with_jmespath("cookies.user_persistence","UserPersistence")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("/app")
                .get("/app")
                .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://mubu.com/login/password",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_cookies(
                **{
                    "language": "en-US",
                    "country": "US",
                    "reg_prepareId": "177d1973926-177d1973676-4ab6-9c11-430341609505",
                    "reg_focusId": "9e853826-cbb4-4ab6-9c11-177d1973d24",
                    "SLARDAR_WEB_ID": "d07bcb26-1fe3-447a-95c5-bb7a30c90c80",
                    "Jwt-Token": "${JwtToken}",
                    "user_persistence": "${UserPersistence}",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/v3/api/message/get_message_unread")
                .post("https://api2.mubu.com/v3/api/message/get_message_unread")
                .with_headers(
                **{
                    "content-length": "10",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${JwtToken}",
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-request-id": "72a597ff-9201-4f8b-8157-594c3c1e1dfe",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/app",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"page": 1})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/profile")
                .post("https://api2.mubu.com/v3/api/user/profile")
                .with_headers(
                **{
                    "content-length": "0",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${JwtToken}",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-request-id": "f6d7d56f-157c-4b8e-aea6-b680d15bd883",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/app",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_data("")
                .extract()
                .with_jmespath("body.data.id","userId")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/get_all_documents_page")
                .post("https://api2.mubu.com/v3/api/list/get_all_documents_page")
                .with_headers(
                **{
                    "content-length": "12",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${JwtToken}",
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-request-id": "ce83494c-d5c8-40ab-a8ac-e7a5d6d84bb4",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/app",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"start": ""})
                .teardown_hook("${get_documents_num($response)}","document_num")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_greater_than("$document_num",2)
        ),
        Step(
            RunRequest("/v3/api/list/star_relation/get")
                .get("https://api2.mubu.com/v3/api/list/star_relation/get")
                .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${JwtToken}",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-request-id": "0a3e8a01-5c63-4a7b-bfa4-fd666f67a397",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/app",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/advertisement/get")
                .post("https://api2.mubu.com/v3/api/advertisement/get")
                .with_headers(
                **{
                    "content-length": "10",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${JwtToken}",
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-request-id": "4ab1f58f-860f-47f5-9093-a9ba5f9e74e8",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/app",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"type": 1})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
                .post("https://api2.mubu.com/v3/api/list/item_count")
                .with_headers(
                **{
                    "content-length": "30",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${JwtToken}",
                    "content-type": "application/json;charset=UTF-8",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-request-id": "31e3c77b-ce95-4a54-85ff-3d34c53c45a6",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/app",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"folderId": 0, "source": "home"})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/get_user_params")
                .post("https://api2.mubu.com/v3/api/user/get_user_params")
                .with_headers(
                **{
                    "content-length": "0",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "${JwtToken}",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-request-id": "80ad480c-7828-471f-8500-c979ae0e5a7f",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/app",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_data("")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
    ]

if __name__ == "__main__":
    TestCaseMubuLogin().test_start()
