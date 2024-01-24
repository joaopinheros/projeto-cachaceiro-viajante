Olá, sejam bem vindos ao meu projeto do cachceiro viajante!

Contextualização:

  O problema do Cachaceiro Viajante é uma variação do tradicional Problema do Caixeiro Viajante com restrição de visitar todos os bares.
  No entanto, nesta versão, introduzimos uma restrição adicional: o viajante deve visitar todos os bares da cidade antes de concluir sua jornada.

Restrições:
  1. Visita a todos os bares:
     A restrição central deste problema é que o caixeiro viajante deve visitar todos os bares da cidade antes de encerrar sua jornada.
     Isso significa que cada bar deve ser incluído na rota.
     
  2. Minimização da distância total:
     Como no problema original do Caixeiro Viajante, o objetivo secundário é minimizar a distância total percorrida ao visitar os bares.
     Portanto, a rota deve ser otimizada para ser a mais curta possível.
     
  3. Determinação da ordem de visitas:
     A ordem em que os bares são visitados é uma variável importante. Isso implica que o viajante deve decidir qual bar visitar a seguir,
     levando em consideração a localização dos bares e a otimização da distância total percorrida.
     
  4. Retorno ao ponto de partida:
     Como em todas as versões do problema do Caixeiro Viajante, o viajante deve retornar ao ponto de partida para concluir sua jornada
     após visitar todos os bares.
     
  5. Complexidade computacional:
     À medida que o número de bares na cidade aumenta, a complexidade computacional do problema também cresce de forma exponencial,
     tornando a busca pela solução ótima desafiadora.

Para dar um toque especial, introduzimos a ideia de que o caixeiro viajante fica mais tonto a cada bar visitado. Isso acrescentaria um novo elemento
à otimização da rota, uma vez que o objetivo seria minimizar a "intoxicação" total ao mesmo tempo que ele visita todos os bares. Seguimos os seguintes critérios: 


  1. Variável de "Intoxicação": Introduzimos uma variável que represente o nível de "intoxicação" do caixeiro viajante.
     Inicialmente, essa variável é definida como zero, já que ele ainda não consumiu nenhuma bebida.
     À medida que ele visita cada bar, esse valor aumenta com base na quantidade de bebida consumida,
     multiplicada por um fator que representaria o impacto na sua intoxicação.
     
  2. Fator de Impacto da Bebida: Atribuímos a cada tipo de bebida ou a cada quantidade de bebida uma taxa de impacto na intoxicação do caixeiro.
     Bebidas mais fortes ou uma maior quantidade de bebida teriam um fator de impacto mais elevado.
     
  3. Restrições da Intoxicação: Definimos um limite máximo para o nível de intoxicação que o caixeiro viajante pode atingir antes de não conseguir continuar.
     Isso adiciona uma restrição ao problema, pois ele deve planejar sua rota de forma a não exceder esse limite em nenhum momento.
     
  4. Função de Avaliação: “O Cachaceiro Viajante” deve levar em consideração tanto a distância percorrida como a intoxicação.
     A função de avaliação agora deve ponderar a minimização da distância e a minimização da intoxicação.
     Isso significa que a solução ótima será aquela que permite ao caixeiro visitar todos os bares sem ficar excessivamente intoxicado e percorrendo a menor distância

Espero que gostem!! 
