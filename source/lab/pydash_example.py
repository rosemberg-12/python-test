import typing
import json
import pydantic
import pydash

class SeonEvaluateResponse(pydantic.BaseModel):
    id: str
    fraud_score: int
    bin_details: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    applied_rules: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]
    device_details: typing.Optional[typing.Any]
    calculation_time: typing.Optional[int]
    seon_id: str
    ip_details: typing.Optional[typing.Dict[str, typing.Any]]
    email_details: typing.Optional[typing.Dict[str, typing.Any]]
    phone_details: typing.Optional[typing.Dict[str, typing.Any]]

            
    def hola():
        return True
    
    def is_location_info_data_valid(self):
        return True
    
            
    def _is_location_info_data_valid():
        return True

seon_response = MOCK_WEB_PAYMENT_SEON_RESPONSE_COMPLETE = {
    "id": "XXXXXXXX",
    "state": "APPROVE",
    "seon_id": 13011,
    "version": "v2.0",
    "ip_details": {
        "ip": "999.99.999.999",
        "tor": False,
        "vpn": False,
        "city": "Rionegro",
        "type": "MOB",
        "score": 0,
        "country": "CO",
        "isp_name": "Colombia Movil",
        "latitude": 6.1551,
        "longitude": -75.3737,
        "spam_urls": [],
        "web_proxy": False,
        "open_ports": [],
        "state_prov": "Antioquia",
        "spam_number": 0,
        "public_proxy": False,
        "timezone_offset": "-05:00",
    },
    "bin_details": {
        "bin_bank": "BANCO XXX.",
        "bin_card": "VISA",
        "bin_type": "CREDIT",
        "card_bin": "999999",
        "bin_level": "CLASSIC",
        "bin_phone": "(1)999999 -999999",
        "bin_valid": True,
        "bin_country": "COLOMBIA",
        "bin_website": "www.scotiabankcolpatria.com",
        "card_issuer": "VISA",
        "bin_country_code": "CO",
    },
    "fraud_score": 2,
    "applied_rules": [
        {
            "id": "XXXXX",
            "name": "Suspicious browser profile - Privacy extension",
            "score": 2,
            "operation": "+",
        }
    ],
    "email_details": {
        "email": "testing.fv2@gmail.com",
        "score": 2.1100000000000003,
        "deliverable": True,
        "domain_details": {
            "domain": "gmail.com",
            "tld": ".com",
            "registered": True,
            "created": "1995-08-13 04:00:00",
            "updated": "2022-07-11 09:25:59",
            "expires": "2023-08-12 04:00:00",
            "registrar_name": "MarkMonitor Inc.",
            "registered_to": "Google LLC",
            "disposable": False,
            "free": True,
            "custom": False,
            "dmarc_enforced": True,
            "spf_strict": True,
            "valid_mx": True,
            "accept_all": False,
            "suspicious_tld": False,
            "website_exists": True,
        },
        "account_details": {
            "apple": {"registered": False},
            "ebay": {"registered": None},
            "facebook": {"registered": False, "url": None, "name": None, "photo": None},
            "flickr": {"registered": False},
            "foursquare": {"registered": False},
            "github": {"registered": False},
            "google": {"registered": True, "photo": None},
            "gravatar": {"registered": False},
            "instagram": {"registered": None},
            "lastfm": {"registered": None},
            "linkedin": {
                "registered": None,
                "url": None,
                "name": None,
                "company": None,
                "title": None,
                "location": None,
                "website": None,
                "twitter": None,
                "photo": None,
            },
            "microsoft": {"registered": False},
            "myspace": {"registered": False},
            "pinterest": {"registered": False},
            "skype": {
                "registered": False,
                "country": None,
                "city": None,
                "gender": None,
                "name": None,
                "id": None,
                "handle": None,
                "bio": None,
                "age": None,
                "language": None,
                "state": None,
                "photo": None,
            },
            "spotify": {"registered": False},
            "tumblr": {"registered": False},
            "twitter": {"registered": False},
            "vimeo": {"registered": None},
            "weibo": {"registered": False},
            "yahoo": {"registered": None},
        },
        "breach_details": {
            "haveibeenpwned_listed": False,
            "number_of_breaches": 0,
            "first_breach": None,
            "breaches": [],
        },
    },
    "phone_details": None,
    "device_details": {
        "os": "iOS",
        "type": "web",
        "dns_ip": "190.240.112.183",
        "source": "js-5.6.0",
        "adblock": False,
        "browser": "MOBILE_SAFARI",
        "private": False,
        "platform": "iPhone",
        "font_hash": "00000000000000000000000000000000",
        "font_list": [],
        "audio_hash": "124.0434496849557",
        "dns_ip_isp": "EPM Telecomunicaciones S.A. E.S.P.",
        "font_count": 0,
        "session_id": "1N498074RB_d2b4e53f-e16f-4f52-9ff2-c6656a6c3f7e",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1",
        "webgl_hash": "f73f81dc835f9c403907fdbc5b019eb0",
        "webrtc_ips": ["179.15.250.199", "0.0.0.0"],
        "canvas_hash": "ce23375d97b2001530bd85b71e712c41",
        "cookie_hash": "3ef19a83343f485e0dae538fa64bd318",
        "device_hash": "e4c2d63d41b431ad562a8d85c8a82d57",
        "device_type": "phone",
        "plugin_hash": None,
        "plugin_list": [],
        "window_size": "414x721",
        "browser_hash": "a195977ac5d9bdad447d62ea127beddc",
        "do_not_track": None,
        "java_enabled": False,
        "plugin_count": 0,
        "webgl_vendor": "Apple Inc.~Apple GPU",
        "webrtc_count": 2,
        "battery_level": None,
        "device_ip_isp": "Colombia Movil",
        "device_memory": None,
        "flash_enabled": False,
        "social_logins": [],
        "touch_support": True,
        "cookie_enabled": True,
        "dns_ip_country": "CO",
        "accept_language": [],
        "browser_version": "16.3",
        "region_language": "es-419",
        "region_timezone": "-05:00",
        "battery_charging": None,
        "webrtc_activated": True,
        "device_ip_address": "179.15.250.199",
        "device_ip_country": "CO",
        "screen_resolution": "414x896",
        "screen_color_depth": 32,
        "screen_pixel_ratio": 2,
        "hardware_concurrency": 4,
        "screen_available_resolution": "414x896",
    },
    "calculation_time": 318,
}


SEON_PAYMENT_EVALUATION_EVENT_ITEMS = [
    "id",
    "ip_details.tor",
    "ip_details.vpn",
    "ip_details.city",
    "ip_details.score",
    "ip_details.country",
    "ip_details.isp_name",
    "ip_details.web_proxy",
    "ip_details.state_prov",
    "ip_details.public_proxy",
    "bin_details.bin_bank",
    "bin_details.bin_card",
    "bin_details.bin_type",
    "bin_details.bin_level",
    "bin_details.bin_valid",
    "bin_details.bin_country",
    "fraud_score",
    "applied_rules",
    "email_details.email",
    "email_details.score",
    "email_details.deliverable",
    "email_details.domain_details.custom",
    "email_details.domain_details.disposable",
    "email_details.account_details.facebook",
    "email_details.account_details.linkedin",
    "email_details.account_details.instagram",
    "email_details.account_details.skype",
    "device_details.os",
    "device_details.type",
    "device_details.browser",
    "device_details.platform",
    "device_details.cookie_hash",
    "device_details.device_hash",
    "device_details.device_type",
]



seon_evaluate_payment_response = SeonEvaluateResponse.parse_obj(
    seon_response
)

print(seon_evaluate_payment_response)

seon_response_dict = seon_evaluate_payment_response.dict()
seon_response_dict = pydash.pick(
            seon_response_dict, SEON_PAYMENT_EVALUATION_EVENT_ITEMS
    )

print("Nuevo response")
print("Nuevo response")
print("Nuevo response")
print(seon_response_dict)


class ReconocerAccessTokenResponse(pydantic.BaseModel):
    access_token: str
    token_type: str
    expires_in: str
    scope: str



variable = '{"access_token": "eyJraWQiOiJOSHJxY1h3ei1XTF96aXlybWJ4bzROdnZpMEFkQkpreUVTZUF6cHYxRzlJIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmtzNlpqRGcwekN2R0hBWlZvNTU3N0FPSm5lbTR0R2t0aDdaLUt2VHkzaDAiLCJpc3MiOiJodHRwczovL2V4cGVyaWFuLWxhdGFtYi5va3RhcHJldmlldy5jb20vb2F1dGgyL2F1c2Rid2k3cGVzNzFuMGhVMGg3IiwiYXVkIjoiaHR0cHM6Ly93d3cuZGF0YWNyZWRpdG8uY29tLmNvL2NsaWVudHMiLCJpYXQiOjE1MjM2NDY0NTMsImV4cCI6MTUyMzY1MDA1MywiY2lkIjoiMG9hZW9mZ2d6dVNpZ3NkOEIwaDciLCJ1aWQiOiIwMHU4eWI3NDBqNG15amhEVDBoNyIsInNjcCI6WyJleHBfY29fc2xhX3JlY29ub2Nlcl9tYXN0ZXJfYXV0aHoiXSwic3ViIjoiMS03OTYyODc0OUBkZXYuZGF0YWNyZWRpdG8uY29tLmNvIn0.gkmtEa2wKNrEEPEH3NkMFN_TIxFCx9evCs8J1KJAtLSqU-HcKZQ4mVk4u-VHlglQ369GDQ7jcGwTFVm72FiNbNyR-3aSCj8XprQHVsnpQPEbcamrdP8CvYSWi9z-onfSL4wtWp0uvYMKgwyWvbSm2-tfvLlKwGylfc7vec97Wd0RnsD-W3GpeYw_JztEUBhrk-C54374Xzmap_D8ShrSmnw7gibPHTftfs6ixhQwR4OzT2W64d3hZPTzYfc6c9efF-MBVUYTX7GQgGHt-269epUiz6ReSKAlQQilh1hzA2nJ7SeGyz2S80DZGbucnxIyievbJ15MmPe_DbhYHYmOMQ", "token_type": "Bearer", "expires_in": 3600, "scope": "exp_co_sla_reconocer_master_authz"}'
print(ReconocerAccessTokenResponse.parse_obj(variable))

        
def _is_location_info_data_valid(self, typing.Dict[str, typing.Any]) -> bool:
    return True