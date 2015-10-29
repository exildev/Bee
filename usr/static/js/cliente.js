/**
 * Created by dreicon88 on 25/04/15.
 */
var cliente;
$(document).on('ready',function(){
    cliente = $("#add_cliente:first").dialog({
        autoOpen: false,
        draggable: false,
        modal:true,
        width:540,
        heigth:331,
        show: {
            effect: "slideDown",
            duration: 200
        },
        hide: {
            effect: "slideUp",
            duration: 200
        },
        buttons: {
            "Guargar":function(){
                add_cliente();
            },
            "Cancelar":function(){
                $('#login').show();
            	$(this).dialog("close");
            }
        },
        close:function(){
            $('#login').show();
        	$(this).dialog('close')
        }
    });
    $('.cliente').on('click',function(){
        $('#login').hide();
        $('#add_cliente #cont').load('/usr/add/cliente/',function(){
            cliente.dialog('open');
        });

    });
});

function add_cliente(){
    $.post( "/usr/add/cliente/", $('#add_cliente #cont form').serialize(),function(data){
        if(data[0].r){
            $('input[name="username"]').val(data[0].n);
            $('input[name="password"]').val(data[0].c);
            cliente.dialog("close");
            $('#login form').submit();
        }else{
            $('#add_cliente #cont').empty().append(data);
        }
    });
}