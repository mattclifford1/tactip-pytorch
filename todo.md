# List of Dev todos
CODE validation
- compare MAE of keras model to torch model (keras: https://data.bris.ac.uk/data/dataset/110f0tkyy28pa2joru2pxxbrxd)
  - keras data from above url:
    - edge_2d:    [2, 6]  [0.15, 1.45]     331: [0.15, 1.66]
    - surface_2d: [2, 6]  [0.08, 0.72]     331: [0.11, 0.73]


plotting
- combine multiple runs



dataloader
(maybe change to just using the sim2real data?)
  - simpler image loading mechanism (remove weight transforms shite)


network
- flexible to let user define different conv channel sizes



validaiton
- write tests
- script to eval
  - give model dir and dataloader - return MAE

  - copy over to sim2real and use to evaluate real2sim output


over-arching
- restructure repo into folders
- make into a pipeline
- add detailed readme
