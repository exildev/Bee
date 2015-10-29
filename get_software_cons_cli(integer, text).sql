-- Function: get_software_cons_cli(integer, text)

-- DROP FUNCTION get_software_cons_cli(integer, text);

CREATE OR REPLACE FUNCTION get_software_cons_cli(
    id_user integer,
    reque text)
  RETURNS json AS
$BODY$
begin
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		
		select distinct on(s.id) s.id as pk,s.imagen,s.nombre,regexp_replace(s.descripcion,'(\n|\r|\t)+','<br>') as descripcion,case when sol.estado = true then
		  'Asignado' 
		 when sol.estado = false then
		  'Solicitado' 
		  else
		   'Solicitar'
		   end,
		   case when sol.estado = true then
		 2
		 when sol.estado = false then
		  1
		  else
		   0
		   end as estado,
		   case when int8(sol.id)= sol.id then 
		    sol.id
		    else 
		    0 
		    end as id_res 
		 from vista_requerimiento as r 
		join bee_software_requerimientos as sr on(r.requerimiento_id=sr.requerimiento_id and sr.requerimiento_id=any(reque::int[])) 
		join bee_software as s on( s.id=sr.software_id) 
		left join bee_solicitud as sol on(s.id=sol.software_id and sol.cliente_id=id_user) order by s.id
	) p);
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION get_software_cons_cli(integer, text)
  OWNER TO postgres;
