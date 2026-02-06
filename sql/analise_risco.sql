/* --------------------------------------------------------------------------
   ANÁLISE 1: A SAÚDE DA CARTEIRA (SEGMENTAÇÃO POR USO)
   Pergunta: Como está a distribuição dos clientes baseada no uso do limite?
   Insight: A maioria dos clientes é saudável (Grupo 3), mas o grupo de "Alerta"
            preocupa pelo alto volume de saques em dinheiro.
   -------------------------------------------------------------------------- */
SELECT 
    CASE 
        WHEN (balance / credit_limit) >= 0.9 THEN '1. Crítico'
        WHEN (balance / credit_limit) BETWEEN 0.5 AND 0.89 THEN '2. Alerta (Uso Alto)'
        WHEN (balance / credit_limit) < 0.5 AND purchases > 0 THEN '3. Saudável (Bom Pagador)'
        ELSE '4. Inativo/Baixo Uso'
    END AS perfil_cliente,
    
    COUNT(*) AS total_clientes,
    ROUND(AVG(credit_limit), 2) AS media_limite,
    ROUND(AVG(balance), 2) AS media_divida,
    ROUND(AVG(cash_advance), 2) AS media_saque 
FROM tb_clientes_credito
WHERE credit_limit > 0
GROUP BY 1
ORDER BY 1;

/* --------------------------------------------------------------------------
   ANÁLISE 2: O COMPORTAMENTO DE RISCO (SAQUE / CASH ADVANCE)
   Hipótese: O uso de saque em dinheiro (Cash Advance) indica risco de inadimplência?
   Validação: Sim. Clientes que estouram o limite sacam, em média, 4x mais dinheiro
              do que os clientes que se mantêm dentro do limite.
   -------------------------------------------------------------------------- */
SELECT 
    CASE 
        WHEN (balance / credit_limit) > 1 THEN 'Estourou o Limite (>100%)'
        ELSE 'Dentro do Limite'
    END AS status_limite,
    
    COUNT(*) AS total_clientes,
    ROUND(AVG(cash_advance), 2) AS media_saques_dinheiro
FROM tb_clientes_credito
WHERE credit_limit > 0
GROUP BY 1;

/* --------------------------------------------------------------------------
   ANÁLISE 3: RISCO POR FAIXA DE LIMITE (PROXY DE RENDA)
   Pergunta: Clientes com limites maiores são mais seguros para o banco?
   Insight: Sim. O risco de estouro cai drasticamente conforme o limite aumenta.
            - Baixo Limite: ~20% de taxa de risco.
            - Alto Limite: ~4% de taxa de risco.
   -------------------------------------------------------------------------- */
SELECT 
    CASE 
        WHEN credit_limit <= 2500 THEN '1. Baixa Renda (Est. Limite Baixo)'
        WHEN credit_limit BETWEEN 2500.01 AND 7000 THEN '2. Média Renda (Est. Limite Médio)'
        ELSE '3. Alta Renda (Est. Limite Alto)'
    END AS faixa_poder_aquisitivo,
    
    -- Taxa de clientes com uso acima de 90%
    ROUND(CAST(SUM(CASE WHEN (balance / credit_limit) >= 0.9 THEN 1 ELSE 0 END) AS FLOAT) 
          / COUNT(*) * 100, 2) || '%' AS taxa_alto_risco,
          
    COUNT(*) AS total_clientes,
    ROUND(AVG(balance), 2) AS media_divida
FROM tb_clientes_credito
WHERE credit_limit > 0
GROUP BY 1
ORDER BY 1;