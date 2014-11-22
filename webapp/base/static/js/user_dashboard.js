$(document).ready(function() {
    function block_form() {
        $("#loading").show();
        $('textarea').attr('disabled', 'disabled');
        $('input').attr('disabled', 'disabled');
        $('select').attr('disabled', 'disabled');
    }

    function unblock_form() {
        $('#loading').hide();
        $('textarea').removeAttr('disabled');
        $('input').removeAttr('disabled');
        $('select').removeAttr('disabled');
    }

    var options = {
        beforeSubmit: function(form, options) {
            block_form();
        },
        success: function() {
            $('select').prop('selectedIndex', 0);
            $('textarea').text('');
            $('input[type=text]').val('');
            unblock_form();
        },
        error:  function(resp) {
            unblock_form();
        }
    };

    $('#team_form').ajaxForm(options);

    $('#page-tabs a').click(function (e) {
        e.preventDefault()
        $(this).tab('show')
    })

});
