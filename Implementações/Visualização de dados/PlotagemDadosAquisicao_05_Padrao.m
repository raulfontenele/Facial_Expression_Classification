%% Importação de dados
fname = '../AquisicaoDados/Aquisicao_05/Aquisicao_05_padrao.json';
values = jsondecode(fileread(fname));

%% Plotagem dos gráficos de dispersão
fn = fieldnames(values);
gesto = {'Neutro','Sorriso','Aberto','Grumpy','Surpreso'};
color = {[1 0 0],[0 1 0],[0 0 1],[1 1 0],[1 0 1],[0 1 1],[0 0 0],[0.5 0.5 0.5],[0.5 0.9 0.3],[0.9 0.5 0.3]};
for j = 1:5
    figure();
    for rodada = 1:10
        %subplot(4,3,rodada);
        if isfield(values.(fn{rodada}),gesto{j}) == 1
            scatter(values.(fn{rodada}).(gesto{j})(1,:),values.(fn{rodada}).(gesto{j})(2,:),20,color{rodada},'filled');
            hold on;
            grid;
            title(["Gesto " gesto{j} " - Dataset5 / " fn{rodada} " - Padrão"]);
        end
    end
end


%% Plotagem de dados em relação ao tempo
tempo = 0:0.003:0.003*1599;
fn = fieldnames(values);
gesto = {'Neutro','Sorriso','Aberto','Grumpy','Surpreso'};
color = {[1 0 0],[0 1 0],[0 0 1],[1 1 0],[1 0 1],[0 1 1],[0 0 0],[0.5 0.5 0.5],[0.5 0.9 0.3],[0.9 0.5 0.3]};
for j = 1:5
    figure();
    for rodada = 1:10
        subplot(4,3,rodada);
        if isfield(values.(fn{rodada}),gesto{j}) == 1
            plot(tempo,values.(fn{rodada}).(gesto{j})(1,:),tempo,values.(fn{rodada}).(gesto{j})(2,:));
            grid;
            title(["Gesto " gesto{j} " - Dataset5 / " fn{rodada} " - Padrão"]);
            %hold on;
        end
    end
end

%% Plotagem dos gráficos de dispersão de todas as rodadas
fn = fieldnames(values);
gesto = {'Neutro','Sorriso','Aberto','Grumpy','Surpreso'};
color = {[1 0 0],[0 1 0],[0 0 1],[1 1 0],[1 0 1],[0 1 1],[0 0 0],[0.5 0.5 0.5],[0.5 0.9 0.3],[0.9 0.5 0.3]};
for rodada = 1:7

    %figure();
    for j = 1:5
        %subplot(4,3,rodada);
        if isfield(values.(fn{rodada}),gesto{j}) == 1
            scatter(values.(fn{rodada}).(gesto{j})(1,:),values.(fn{rodada}).(gesto{j})(2,:),30,color{j},'filled');
            hold on;

        end
    end
    grid;
    %title("Gesto faciais");
    xlabel("Sensor 1");
    ylabel("Sensor 2");
    legend(gesto);
end