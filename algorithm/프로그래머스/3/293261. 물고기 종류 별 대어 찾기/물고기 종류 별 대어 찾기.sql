select fi.id, fni.fish_name, fi2.length
from fish_info fi
join (
    select fish_type, max(length) as length
    from fish_info
    group by fish_type
) fi2 on fi.fish_type = fi2.fish_type and fi.length = fi2.length
join fish_name_info fni on fi.fish_type = fni.fish_type
order by fi.id
;