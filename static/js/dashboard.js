jQuery(document).ready(function($) {
    $('#university').click(function() {
        var $this = $(this);
        if ($this.is(':checked')) {
            console.log('check');
        } else {
            console.log('uncheck');
        }
    });
});
