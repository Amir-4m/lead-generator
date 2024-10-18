window.domainSetup = 'https://apps.growmeorganic.com';
window.apiKeyTokenKLM87 = '1b8469747966f26a76b1acce1db275cf-79f4c5b4834038ebc5a7c02e29fad673';
window.apiKeyTokenKLM88 = '64d3c0003f3cf52a3d8b565a';

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
