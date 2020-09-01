%% Importação de dados
fname = '../AquisicaoDados/Aquisicao_05/Aquisicao_05_transicoes.json';
values = jsondecode(fileread(fname));

%% Plotagem dos gráficos de dispersão
fn = fieldnames(values);
gesto = {'Neutro','Sorriso','Aberto','Grumpy','Surpreso'};
color = {[1 0 0],[0 1 0],[0 0 1],[1 1 0],[1 0 1],[0 1 1],[0 0 0],[0.5 0.5 0.5],[0.5 0.9 0.3],[0.9 0.5 0.3]};
for j = 1:5
    figure();
    for rodada = 1:7
        %subplot(4,2,rodada);
        if isfield(values.(fn{rodada}),gesto{j}) == 1
            scatter(values.(fn{rodada}).(gesto{j})(1,:),values.(fn{rodada}).(gesto{j})(2,:),20,color{rodada},'filled');
            hold on;
            grid;
            title(["Gesto " gesto{j} " - Dataset5 / " fn{rodada} " - Transições"]);
            xlabel("Sensor 1")
            ylabel("Sensor 2")
        end
    end
end


%% Plotagem de dados em relação ao tempo
tempo = 0:0.003:0.003*2999;
fn = fieldnames(values);
gesto = {'Neutro','Sorriso','Aberto','Grumpy','Surpreso'};
color = {[1 0 0],[0 1 0],[0 0 1],[1 1 0],[1 0 1],[0 1 1],[0 0 0],[0.5 0.5 0.5],[0.5 0.9 0.3],[0.9 0.5 0.3]};
for j = 1:5
    %figure();
    for rodada = 1:7
        %subplot(4,2,rodada);
        figure();
        if isfield(values.(fn{rodada}),gesto{j}) == 1
            plot(tempo,values.(fn{rodada}).(gesto{j})(1,:),tempo,values.(fn{rodada}).(gesto{j})(2,:));
%             stem(tempo,values.(fn{rodada}).(gesto{j})(1,:));
%             hold on;
%             stem(tempo,values.(fn{rodada}).(gesto{j})(2,:));
            grid;
            xlabel("Tempo")
            ylabel("Amplitude")
            legend({'Sensor bochecha','Sensor testa'});
            title(["Gesto " gesto{j} " - Dataset5 / " fn{rodada} " - Transições"]);
        end
    end
end

%% Plotagem de dados em relação ao tempo
tempo = 0:0.003:0.003*2999;
fn = fieldnames(values);
gesto = {'Neutro','Sorriso','Aberto','Grumpy','Surpreso'};
color = {[1 0 0],[0 1 0],[0 0 1],[1 1 0],[1 0 1],[0 1 1],[0 0 0],[0.5 0.5 0.5],[0.5 0.9 0.3],[0.9 0.5 0.3]};
for rodada = 1:7
    figure();
    for j = 1:5
        subplot(5,1,j);
        plot(tempo,values.(fn{rodada}).(gesto{j})(1,:),tempo,values.(fn{rodada}).(gesto{j})(2,:),'linewidth',2.5);
        grid;
        xlabel("Tempo(s)")
        ylabel("Amplitude")
        legend({'Sensor bochecha','Sensor testa'});
        title(["Gesto " gesto{j}]);
    end
end

