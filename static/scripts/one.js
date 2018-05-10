$(document).ready( function() {

    $(".action").click(function() {
        var applier_id;
        applier_id = $(this).attr("id");
        
        getAction(applier_id);
    });

    function getAction(applier_id) {
        $(".approve").click(function() {
            var ap_action;
            ap_action = $(this).attr("value");

            $.ajax({url: "/jportal/job_applications/",
                data: { status: ap_action, applier: applier_id },
                success: function(result){
                    $(document).find('#' + applier_id).text('Approved');
                    console.log("Server response", JSON.parse(result));
                }
            });
        });

        $(".reject").click(function() {
            var ap_action;
            ap_action = $(this).attr("value");

            $.ajax({url: "/jportal/job_applications/",
                data: { status: ap_action, applier: applier_id },
                success: function(result){
                    $(document).find('#' + applier_id).text('Rejected');
                    console.log("Server response", JSON.parse(result));
                }
            });
        });
    }

});
