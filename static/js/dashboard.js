jQuery(document).ready(function($) {

	$("#jobOptions").on("click", applyForm);

	$("#applySelected").on('click', function(event){
		var jobPosts = $(".jobPosts");
		jobPosts.each(function(i, jobPost){
			console.log("clicking on jobPost!");
			if($("willApply:checked").length === 1) {
				applyForm();
			}
		});
		return false;
	});

	$("#applyAllJobs").on('click', function(e){
		var jobPosts = $(".jobPosts");
		console.log(jobPosts);
		$(".jobPosts").each(function(i, jobPost){
			console.log("clicking on jobPost!");
			applyForm(e);
		});
		return false;
	});


function applyForm(e){
	console.log("applying!");
	$("#apply").attr("id","applied");
	$("#apply").html("Applied");
	$("#checkmark").show();
	$("#checkmark").attr("display", "inline");
	e.preventDefault();
	return false;
}

    $('#university').click(function() {
        var $this = $(this);
        if ($this.is(':checked')) {
            var filter = $("#uni-options :selected").text();
            $('.job-uni').each(function(i, obj) {
                 if ($(this).html().indexOf(filter) == -1) {
                    $(this).parents(".jobPost").hide();
                 }
            });
        } else {
            $('.job-uni').each(function(i, obj) {
                $(this).parents(".jobPost").show();
            });
        }
    });

    $('#uni-options').change(function() {
        var filter = $("#uni-options :selected").text();
        $('.job-uni').each(function(i, obj) {
             if ($(this).html().indexOf(filter) == -1) {
                $(this).parents(".jobPost").hide();
             } else {
                $(this).parents(".jobPost").show();
             }
        });
    });

});
