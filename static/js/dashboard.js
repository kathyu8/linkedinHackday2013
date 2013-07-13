$(window).load = function() {
	$("#apply").click(applyForm);

	$("#applySelected").click(function(){
		var jobPosts = $("#jobPosts");
		jobPosts.each(function(i, jobPost){
			console.log("clicking on jobPost!");
			if($("willApply:checked").length === 1) {
				applyForm();
			}
			return false;
		});
	});

	$("#applyAll").click(function(){
		var jobPosts = $("#jobPosts");
		jobPosts.each(function(i, jobPost){
			console.log("clicking on jobPost!");
			applyForm();
		});
		return false;
	});
}

function applyForm(){
	console.log("applying!");
	$("#apply").attr("id","applied");
	$("#apply").html("Applied");
	$("#checkmark").show();
	$("#checkmark").attr("display", "inline");
	return false;
}

jQuery(document).ready(function($) {
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
