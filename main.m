>> % Define the commute time data as adjacency matrices for both cases
% '-' values are represented as 0 (no direct path)

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

% Labels for points
labels = {"National College", "Ramakrishna Circle", "Tagore Circle", "Bull Temple", ...
          "NR Colony", "Hanumantha Nagar Ward Office", "Front Gate", "Back Gate"};

% Function to compute and visualize shortest paths
function visualize_shortest_paths(adj_matrix, labels, case_name)
    num_nodes = size(adj_matrix, 1);
    G = graph(adj_matrix, labels, 'upper');

    for source = 1:num_nodes
        for target = 1:num_nodes
            if source ~= target
                % Compute shortest path
                [path, path_len] = shortestpath(G, source, target);
                
                % Visualize the graph with the shortest path highlighted
                figure;
                p = plot(G, 'EdgeLabel', G.Edges.Weight, 'LineWidth', 1.5, 'NodeFontSize', 10);
                highlight(p, path, 'EdgeColor', 'r', 'LineWidth', 2.5);
                title(sprintf('Shortest Path from %s to %s (%s)\nLength: %.2f', ...
                      labels{source}, labels{target}, case_name, path_len));

                % Save the figure
                saveas(gcf, sprintf('shortest_path_%s_%s_to_%s.png', case_name, labels{source}, labels{target}));
                close;
            end
        end
    end
end

% Compute shortest paths for both cases
visualize_shortest_paths(commute_parish, labels, 'during_parish');
visualize_shortest_paths(commute_ordinary, labels, 'ordinary_days');

 function visualize_shortest_paths(adj_matrix, labels, case_name)
 ↑
Error: Function definitions are not supported in this context. Functions can only be created as local or nested functions in
code files.
 
>> 
