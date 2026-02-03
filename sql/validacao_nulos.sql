SELECT count(*) as qtd_erros_limite
FROM tb_clientes_credito
WHERE credit_limit IS NULL;