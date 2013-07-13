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
