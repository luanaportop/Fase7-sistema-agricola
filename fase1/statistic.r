dados <- read.csv("fase1dados.csv")

media_area <- mean(dados$area)
media_insumo <- mean(dados$insumo)
desvio_area <- sd(dados$area)
desvio_insumo <- sd(dados$insumo)

resultados <- data.frame(
  Estatística = c("Média da área", "Desvio padrão da área", "Média do insumo", "Desvio padrão do insumo"),
  Valor = c(media_area, desvio_area, media_insumo, desvio_insumo)
)

print(resultados)
write.csv(resultados, "resultados_estatisticos.csv", row.names = FALSE)

