# Facial Expression Classification
  
<div>
  <article>
  O presente repositório apresente as informações relativas ao trabalho de aquisição e classificação de expressões faciais utilizando sinais de Eletromiografia.
  </article>
  <div>
    O trabalho desenvolvido pelos seguintes autores: 
    <ul>
      <li>Paulo Cirillo S. Barboza</li>
      <li>Raul F. Santana</li>
      <li>George A. P. Thé</li>
    </ul>
  </div>
</div>

  
## Organização dos arquivos
<div>
  Os arquivos estão divididos em três pastas principais:
  <ul>
      <li>Aquisição de dados</li>
      <li>Implementações</li>
      <li>Relatórios</li>
    </ul>
  Nessas pastas estão contidos todos os dados necessários para a replicação do experimento relacionado a classificação de expressões.
</div>

<div>
  <h3>Aquisição de dados</h3>
  <article style="text-align: justify">
    Nesse diretório estão contidos os dados decorrentes de duas aquisições de dados: Aquisicao_05 e a Aquisicao_06. Em cada uma das pastas de aquisição estão presentes dados         referentes a aquisições com a expressão mantida ao longo em toda a janela de captura (padrão) e com variações entre a expressão e a expressão base neutra (transições).           Também está presente nesse diretório o <i>dataset</i> criado e utilizado nas etapas de classificação, criado a parte das rodadas de aquisição com a expressão fixa ao longo       de toda a janela de aquisição, bem como informações estatísticas a respeito do mesmo.
  </article>
</div>
<div>
  <h3>Implementações</h3>
  <article style="text-align: justify">
    Nesse diretório estão contidos os <i>scripts</i> utilizados para a a aquisição e classificação dos dados. Os classificadores utilizados foram a rede neural <i>Multilayer         Perceptron</i>, os classificadores de dissimililaridade baseados em distância euclidiana DMC e KNN, e baseado na distância de Mahalannobis CQ, além do algoritmo de regressão linear LQM. Os classificadores possuem duas implementações, realizadas por dois dos autores, na linguagem Python. O código de aquisição de dados é único e implementado c++, compatível com o micro utilizado. Também estão disponíveis <i>scripts</i> para a visualização dos dados.
  </article>
</div>
<div>
  <h3>Relatório</h3>
  <article style="text-align: justify">
    Nesse diretório estão presentes os arquivos com os resultados das execuções de cada um dos classificadores, com sua configuração, taxas de acerto e tempo de execução. Também     estão presentes os arquivos de consolidação, com os resultados dos dois experimentos, bem como as informações estatísticas utilizadas nas tomadas de decisão.
  </article>
</div>




                                                 
                                                 
