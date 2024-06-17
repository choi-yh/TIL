select ed.id, ed.genotype, parent_ed.genotype as parent_genotype
from ecoli_data ed
join ecoli_data parent_ed on parent_ed.id = ed.parent_id
where ed.genotype & parent_ed.genotype = parent_ed.genotype
order by ed.id