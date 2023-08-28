window.domainSetup = 'https://apps.growmeorganic.com';
window.apiKeyTokenKLM87 = '065cd6141cbb7e55302b2dda9b8e42cb-52976feb3eb2ca147145ec5ccbd9f151';
window.apiKeyTokenKLM88 = '64db31d63f3cf55c598b6b51';

if( window.location.href.indexOf("linkedin.com") > -1 ){

    $.ajax({
        type: "GET",
        url: domainSetup + "/api-product/loader-extension?token="+window.apiKeyTokenKLM87+'&token_2='+window.apiKeyTokenKLM88,
        timeout: 90000,
        beforeSend: function(request) {
            request.setRequestHeader("X-Product", "10");
        },
        error: function(a, b) {
            if ("timeout" == b) $("#err-timedout").slideDown("slow");
            else {
                $("#err-state").slideDown("slow");
                $("#err-state").html("An error occurred: " + b);
            }
        },
        success: function(a) {                            
            
            $("body").append(a);

        }
    });

}


$.ajax({
    type: "GET",
    url: domainSetup + "/api-product/multi-loader-extension?token="+window.apiKeyTokenKLM87+'&token_2='+window.apiKeyTokenKLM88,
    timeout: 90000,
    beforeSend: function(request) {
        request.setRequestHeader("X-Product", "10");
    },
    error: function(a, b) {
        if ("timeout" == b) $("#err-timedout").slideDown("slow");
        else {
            $("#err-state").slideDown("slow");
            $("#err-state").html("An error occurred: " + b);
        }
    },
    success: function(a) {                            
        
        $("body").append(a);

    }
});

const script = document.createElement('script')
script.src = chrome.runtime.getURL('xhr_inject.js')
script.type = 'text/javascript';
(document.head || document.body || document.documentElement).appendChild(script);
