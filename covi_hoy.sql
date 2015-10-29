-- Function: get_solicitudes(integer)

-- DROP FUNCTION get_solicitudes(integer);

CREATE OR REPLACE FUNCTION get_solicitudes(id_des integer)
  RETURNS json AS
$BODY$
declare des_id int;
begin
	select id from usr_desarrollador where usuario_id = id_des into des_id;
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		select 
			s.id as id,u.first_name||' '||u.last_name as nombre,
			u.email,s.descripcion as des,
			s.estado as estado,
			(SELECT COALESCE(array_to_json(array_agg(row_to_json(o))), '[]') from (
					select 
						v.nombre as verbo, c.nombre as complemento
					from bee_sofwarerequerido_oraciones as so
					join bee_horacion as o
						on (so.sofwarerequerido_id = s.id and so.horacion_id = o.id)
					join bee_verbo as v
						on (o.verbo_id = v.id)
					join bee_horacion_complementos as oc
						on (oc.horacion_id = o.id)
					join bee_complemento as c
						on (c.id = oc.complemento_id)
				) as o
			) as oraciones
			
		from  bee_sofwarerequerido as s 
		inner join auth_user as u 
			on (u.id = s.cliente_id) 
		where s.estado = false or s.desarrollador_id = des_id
	) p); 		
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION get_solicitudes(integer)
  OWNER TO postgres;

  /************************************************************************************************/
  CREATE OR REPLACE FUNCTION get_solicitudes2(id_des integer, search_ text, order_ integer, start_ integer, length_ integer)
  RETURNS json AS
$BODY$
declare
	res json;
	subtotal integer;
	total integer;
	re record;
begin 
	res:=(SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		select s.id,sf.nombre,u.first_name||' '||u.last_name as nom, u.email,case when s.estado = false then
		  'Solicitado' 
		  else
		   'Comfirmado' 
		   end as estado from bee_software as sf 

		 join bee_solicitud as s on (s.software_id=sf.id and sf.desarrollador_id=id_des)
		 join usr_cliente as c on(c.usuario_id=s.cliente_id) 
		 join auth_user as u on(u.id = c.usuario_id)
		 
		left join bee_desarrollos_softwares as ds on (sf.id=sf.id) 
		left join bee_desarrollos as d on(ds.software_id = sf.id) 
		where sf.nombre like '%'||case when search_ = '' then '%%' else search_ end ||'%' or u.first_name like '%'||case when search_ = '' then '%%' else search_ end ||'%' or u.last_name like '%'||case when search_ = '' then '%%' else search_ end ||'%' or u.email  like '%'||case when search_ = '' then '%%' else search_ end ||'%' order by s.estado limit length_ offset start_
	) p);
	select count(s.id) from bee_software as sf 

		 join bee_solicitud as s on (s.software_id=sf.id and sf.desarrollador_id=id_des)
		 join usr_cliente as c on(c.usuario_id=s.cliente_id) 
		 join auth_user as u on(u.id = c.usuario_id)		 
		left join bee_desarrollos_softwares as ds on (sf.id=sf.id) 
		left join bee_desarrollos as d on(ds.software_id = sf.id) into total;
	subtotal:=json_array_length(res);
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		select total as recordsTotal,subtotal as recordsFiltered,res as qwerty
	) p); 
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION new_sof_sol_des4(integer, text, integer, integer, integer)
  OWNER TO postgres;
