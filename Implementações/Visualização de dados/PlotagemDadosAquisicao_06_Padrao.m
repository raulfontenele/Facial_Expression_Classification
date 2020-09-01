%% Importação de dados
fname = '../AquisicaoDados/Aquisicao_06/Aquisicao_06_padrao.json';
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
            title(["Gesto " gesto{j} " - Dataset6 / " fn{rodada} " - Padrão"]);
        end
    end
end

%% Plotagem de dados em relação ao tempo
tempo = 0:0.003:0.003*999;
fn = fieldnames(values);
gesto = {'Neutro','Sorriso','Aberto','Grumpy','Surpreso'};
%color = {[1 0 0],[0 1 0],[0 0 1],[1 1 0],[1 0 1],[0 1 1],[0 0 0],[0.5 0.5 0.5],[0.5 0.9 0.3],[0.9 0.5 0.3]};
for j = 1:5
    figure();
    for rodada = 1:7
        subplot(4,2,rodada);
        if isfield(values.(fn{rodada}),gesto{j}) == 1
            plot(tempo,values.(fn{rodada}).(gesto{j})(1,:),tempo,values.(fn{rodada}).(gesto{j})(2,:))
%             stem(tempo,values.(fn{rodada}).(gesto{j})(1,:), 'filled');
%             hold on;
%             stem(tempo,values.(fn{rodada}).(gesto{j})(2,:), 'filled');
            grid;
            xlabel("Tempo")
            ylabel("Amplitude")
            title(["Gesto " gesto{j} " - Dataset6 / " fn{rodada} " - Padrão"]);
        end
    end
end
% %% Plotagem de dados em relação ao tempo
% tempo = 0:0.003:0.003*999;
% fn = fieldnames(values);
% gesto = {'Neutro','Sorriso','Aberto','Grumpy','Surpreso'};
% for j = 1:5
%     figure();
%     for rodada = 1:10
%         subplot(4,3,rodada);
%         if isfield(values.(fn{rodada}),gesto{j}) == 1
%             stem(tempo,values.(fn{rodada}).(gesto{j})(1,:),tempo,values.(fn{rodada}).(gesto{j})(2,:));
%             grid;
%             title(["Gesto " gesto{j} " - Dataset6 / " fn{rodada} " - Padrão"]);
%             %hold on;
%         end
%     end
% end

%% Gráficos de dispersão de todos os gestos por rodada
fn = fieldnames(values);
tempo = 0:0.003:0.003*999;

gestos = {'Neutro','Sorriso','Aberto','Grumpy','Surpreso'};
color = {[1 0 0],[0 1 0],[0 0 1],[1 1 0],[1 0 1],[0 1 1],[0 0 0],[0.5 0.5 0.5],[0.5 0.9 0.3],[0.9 0.5 0.3]};
for rodada = 1:length(fn)
    %figure();
    for gesto = 1:length(gestos)
        if isfield(values.(fn{rodada}),gestos{gesto}) == 1
            scatter(values.(fn{rodada}).(gestos{gesto})(1,:),values.(fn{rodada}).(gestos{gesto})(2,:),20,color{gesto},'filled');
            hold on;
            
            xlabel("Sensor 2")
            ylabel("Sensor 1")
            grid;
            legend(gestos);
        
        end
        
    end

end

    xlabel("Sensor 2")
    ylabel("Sensor 1")
    grid;
    legend(gestos);

%% Gráficos de dispersão de todos os gestos das rodadas 6 e 9
fn = fieldnames(values);
tempo = 0:0.003:0.003*999;

gestos = {'Neutro','Sorriso','Aberto','Grumpy','Surpreso'};
color = {[1 0 0],[0 1 0],[0 0 1],[1 1 0],[1 0 1],[0 1 1],[0 0 0],[0.5 0.5 0.5],[0.5 0.9 0.3],[0.9 0.5 0.3]};
label = {'Rodada 6','Rodada 9'};
ctr = 1;
for rodada = [6,9]
    %figure();
    for gesto = 1:length(gestos)
        if isfield(values.(fn{rodada}),gestos{gesto}) == 1
            subplot(2,1,ctr);
            scatter(values.(fn{rodada}).(gestos{gesto})(1,:),values.(fn{rodada}).(gestos{gesto})(2,:),20,color{gesto},'filled');
            hold on;
            
            xlabel("Sensor 2")
            ylabel("Sensor 1")
            grid;
            legend(gestos);
            title(label{ctr});
        end       
    end
    ctr = 2;
end