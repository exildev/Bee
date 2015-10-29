$(document).on('ready',function(event){
    $("#buscar").bind('DOMNodeInserted',function(e){
        if($(e.target).attr("id") == "tabla"){
            console.log("Software a la a medida");
            tablaLoad();
            e.stopPropagation();
            return false;
        }else if($(e.target).attr("id") == "buscar"){
            console.log("Software buscar");
            e.stopPropagation();
        }else if($(e.target).attr("id") == "tabla_solicitud"){
            console.log("Software tabla_solicitud");
            e.stopPropagation();
        }
    });
});

function tablaLoad(){
	window.table = $('#tabla').DataTable({
        "bPaginate": true,
        "bScrollCollapse": true,
        "sPaginationType": "full_numbers",
        "bRetrieve": true,
        "oLanguage": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ Registros",
            "sZeroRecords": "No se encontraron resultados",
            "sInfo": "Mostrando desde _START_ hasta _END_ de _TOTAL_ Registros",
            "sInfoEmpty": "Mostrando desde 0 hasta 0 de 0 Registros",
            "sInfoFiltered": "(filtrado de _MAX_ registros en total)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "oPaginate": {
                "sFirst": "<i>&#xf100;</i>",
                "sPrevious": "<i>&#xf104;</i>",
                "sNext": "<i>&#xf105;</i>",
                "sLast": "<i>&#xf101;</i>"
            }
        },
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "/ws/load/peticiones/"

        },
        "drawCallback": function (row, data) {
            $('.center.estado').on('click',function(){
                estadoRequerimiento($(this).parent().find('input[type="hidden"]'));
            });
        },
        "columns": [
            {
                "data": "nombre"
            },
            {
                "data": "nom"
            },
            {
              "data": "email"  
            },
            {
                "data": "estado",
                "render": function(data, type, full, meta){
                    estudiante = data+" "+full.estudiante__apellidos;
                    return "<input type=\"hidden\" id=req name=req value=\""+full.id+"\"><div class=\"center estado\" ><span class=\"center\">"+data+"</span>";
                }  
            }
        ]
    });
}
