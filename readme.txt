# Redes1---2018.2

Commit das atualizações de 18 de setembro:

Dados: 
	- o nome completo (uma única string),
	- o curso (string),
	- DRE (string),
	- CPF (string),
	- data de nascimento em ints separados (diaN DD, mesN MM, anoN YYYY),
	- e uma string de período atual (YYYY.P),
o programa gera os objetos de texto e cola por cima do fundo, que é um retângulo branco de cantos arredondados e transparência.

Além disso, o programa também cola uma imagem na proporção 3x4 em cima do fundo. Foi deixado em branco o espaço destinado ao QR Code, a ser implementado futuramente. A imagem de fundo e o placeholder de foto eu já fiz e incluí no commit.

Estou pensando em como melhorar os campos de string que envolvem (apenas?) números. CPF e período atual nós podemos até formatar na mão se mudarmos para int, mas não sei o suficiente sobre DRE para garantir que nunca tem letras. Se tiver, não dá. Mas não acho que seja necessário usar int só porque o conjunto de caracteres é composto por apenas dígitos numéricos. Não é como se fosse haver operações algébricas.


