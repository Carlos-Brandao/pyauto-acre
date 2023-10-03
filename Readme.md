Este foi feito para automatizar a coleta de dados de servidores públicos do Governo do Acre, basicamente a mesma estrutura dos outros... Obs: tem duas versões, na operação o "bot" rodava em mais de 20 máquinas e mesmo sendo no mesmo navegador (Chrome) as vezes a quantidade de tabs necessária pra chegar em alguns campos variava, então era só ver qual das duas versões usar em cada caso. 

Nesse código, ele já começa a testar outros links do site para verificar outros casos, como se o site foi expirado ou se houve um bug do servidor

siteExpirado = "https://nconsig4.fenixsoft.com.br/ExpiredSession.aspx"
erroPagina ="Erro de Servidor no Aplicativo '/'."

e a partir disso, quando verificava-se essa ocorrência no if algo diferente do loop convencional era feito.