# Collection tracking prices

This project aims at scrapping the price of my MTG collection along time.

## Roadmap

### Price tracking

- [x] Define the format of the output.
- [x] Find an API in order to get prices over time.
- [ ] Implement a basic architecture that will temporarily define the modularity of the project
- [ ] Implement the first concrete objects for a joujou
- [ ] Write the first tests
- [ ] Create a restricted list of product information
- [ ] Implement a script to request Cardmarket and digest the responses to update the .csv
- [ ] Create statistics over time and store it in order to create a dashboard.

### Collection recognition

- [ ] Create an image recognition model in order to find the card informations.
- [ ] Implement the model and test it until the reach of a satisfactory score.
- [ ] Match the output with the price tracking sub-project.