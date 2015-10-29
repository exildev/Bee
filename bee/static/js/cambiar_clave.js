/**
 * Created by dreicon88 on 25/04/15.
 */
var usuario;
$(document).on('ready',function(){
    usuario = $("#cambio").dialog({
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
                modificar_pass();
            },
            "Cancelar":function(){
            	$(this).dialog("close");
            }
        },
        close:function(){
        	$(this).dialog('close')
        }
    });
    $('.cambio_clave').on('click',function(){
        $('#cambio #cam_cla').load('/usr/pass/cambio/',function(){
            usuario.dialog('open');
        });

    });
});

function modificar_pass(){
    $.post( "/usr/add/cliente/", $('#cambio #cam_cla form').serialize(),function(data){
        if(data[0].r){
            usuario.dialog("close");
            $('#login form').submit();
        }else{
            $('#cambio #cam_cla form').empty().append(data);
        }
    });

}
