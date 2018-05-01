$(document).ready( function() {

    $(".action").click(function() {
        var seeker_id;
        seeker_id = $(this).attr("id");
        job_id = $(this).attr("value");
        getAction(seeker_id, job_id);
    });

    function getAction(seeker_id, job_id) {
        $(".approve").click(function() {
            var ap_action;
            ap_action = $(this).attr("value");

            $.ajax({url: "/jportal/job_approval/",
                data: { status: ap_action, seeker: seeker_id, job: job_id },
                success: function(result){
                    let a = '#' + seeker_id.toString();
                    $(a).html("Approved");
                    console.log("Server response",result);
                }
            });
        });

        $(".reject").click(function() {
            var ap_action;
            ap_action = $(this).attr("value");

            $.ajax({url: "/jportal/job_approval/",
                data: { status: ap_action, seeker: seeker_id, job: job_id },
                success: function(result){
                    let a = '#' + seeker_id.toString();
                    $(a).html("Rejected");
                    console.log("Server response",result);
                }
            });
        });
    }
    

});