$(document).ready(function (){
	$("form").ajaxForm({
		target: '#resultado'
	});
    $('.buscar').on('click',function(){
        $('#form').submit();
    });
    $('#resultado,#buscar').bind('DOMNodeInserted',function(event){
        if(event.target.id == "tabla"){
           $('#buscar table').dataTable();
           $('.estado').on('click',function(){
                var boton = $(this);
                //alert($(this).parent().find('input[name="estado"]').val());
                //alert($(this).parent().find('input[name="resp"]').val());
                if (parseInt($(this).parent().find('input[name="estado"]').val()) ==0){
                    $.ajax({
                        type:'post',
                        dataType:'json',
                        data:{'s':$(this).parent().find('input[type="hidden"]').val()},
                        url:$('#ws_sol_sof').val(),
                        success:function(response){
                            if(response[0]){
                                $('#form').submit();
                            }
                        }
                    });
                }
            });
        }
    });
});

