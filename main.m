% Define the commute time data as adjacency matrices for both cases
% Mirror the values along the diagonal to make it an undirected graph
% During Parish
commute_parish = [
    0, 4, 3, 5, 6, 6, 0, 14;
    4, 0, 5, 6, 11, 5, 0, 10;
    3, 5, 0, 6, 6, 8, 0, 10;
    5, 6, 6, 0, 9, 3, 0, 8;
    6, 11, 6, 9, 0, 6, 0, 7;
    6, 5, 8, 3, 6, 0, 0, 5;
    0, 0, 0, 0, 0, 0, 0, 0;
    14, 10, 10, 8, 7, 5, 0, 0
];

% Ordinary Days
commute_ordinary = [
    0, 4, 4, 6, 7, 7, 7, 9;
    4, 0, 4, 5, 6, 4, 4, 5;
    4, 4, 0, 4, 5, 6, 5, 7;
    6, 5, 4, 0, 5, 2, 3, 6;
    7, 6, 5, 5, 0, 5, 4, 6;
    7, 4, 6, 2, 5, 0, 4, 2;
    7, 4, 5, 3, 4, 4, 0, 0;
    9, 5, 7, 6, 6, 2, 0, 0
];

% Point labels
labels = {"National College", "Ramakrishna Circle", "Tagore Circle", "Bull Temple", "NR Colony", ...
          "Hanumantha Nagar Ward Office", "Front Gate", "Back Gate"};

% Create graphs
G_parish = graph(commute_parish, labels);
G_ordinary = graph(commute_ordinary, labels);

% Compute shortest paths and visualize them for During Parish
for source = 1:length(labels)
    for target = 1:length(labels)
        if source ~= target
            [path, path_length] = shortestpath(G_parish, source, target);
            figure;
            plot(G_parish, 'EdgeLabel', G_parish.Edges.Weight, 'LineWidth', 1.5);
            highlight(pplot(G_parish), path, 'EdgeColor', 'r', 'LineWidth', 2);
            title(sprintf('Shortest Path: %s to %s (During Parish)', labels{source}, labels{target}));
            saveas(gcf, sprintf('shortest_path_during_parish_%d_to_%d.png', source, target));
            close;
        end
    end
end

% Compute shortest paths and visualize them for Ordinary Days
for source = 1:length(labels)
    for target = 1:length(labels)
        if source ~= target
            [path, path_length] = shortestpath(G_ordinary, source, target);
            figure;
            plot(G_ordinary, 'EdgeLabel', G_ordinary.Edges.Weight, 'LineWidth', 1.5);
            highlight(pplot(G_ordinary), path, 'EdgeColor', 'r', 'LineWidth', 2);
            title(sprintf('Shortest Path: %s to %s (Ordinary Days)', labels{source}, labels{target}));
            saveas(gcf, sprintf('shortest_path_ordinary_days_%d_to_%d.png', source, target));
            close;
        end
    end
end
