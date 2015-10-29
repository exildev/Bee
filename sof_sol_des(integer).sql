-- Function: sof_sol_des(integer)

-- DROP FUNCTION sof_sol_des(integer);

CREATE OR REPLACE FUNCTION sof_sol_des(id_des integer)
  RETURNS json AS
$BODY$
begin 
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		select s.id,sf.nombre,u.first_name||' '||u.last_name as nom, u.email,case when s.estado = false then
		  'Solicitado' 
		  else
		   'Comfirmado' 
		   end as estado from bee_desarrollos as d 
		inner join bee_desarrollos_softwares as ds on (d.id=ds.desarrollos_id and d.desarrollador_id=id_des) 
		inner join bee_software as sf on(ds.software_id = sf.id) 
		inner join bee_solicitud as s on (s.software_id=ds.software_id)
		inner join usr_cliente as c on(c.usuario_id=s.cliente_id) 
		inner join auth_user as u on(u.id = c.usuario_id) order by s.estado 
	) p);
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION sof_sol_des(integer)
  OWNER TO postgres;
