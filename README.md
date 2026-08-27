# Text Authorship Classifier

A Python tool that analyzes writing style to predict which of two known authors most likely wrote a given text — a technique known as **stylometry** (authorship attribution based on statistical patterns in language use, rather than content).

## How it works

The model builds a statistical profile of a text across five linguistic dimensions:

- **Word frequency** — how often each word appears
- **Word length distribution** — a tendency toward short vs. long words
- **Stems** — root forms of words (e.g. "interesting" and "interested" both map to "interest"), capturing deeper vocabulary habits beyond surface word forms
- **Sentence length distribution** — inferred from sentence-ending punctuation
- **Punctuation usage** — frequency of each punctuation mark

To compare two texts, the model computes a **log-likelihood similarity score** (a Naive Bayes–style approach) for each of these five dimensions. Given an unlabeled "mystery" text and two candidate source texts, it scores the mystery text against both sources and predicts whichever source it more closely resembles across the majority of the five dimensions.

## Example

```python
source1 = TextModel('source1')
source1.add_string('It is interesting that she is interested.')

source2 = TextModel('source2')
source2.add_string('I am very, very excited about this!')

mystery = TextModel('mystery')
mystery.add_string('Is he interested? No, but I am.')
mystery.classify(source1, source2)
```

A real-world use case included in the code compares excerpts from Winston Churchill and Adolf Hitler as reference sources, then classifies several unlabeled texts against them.

## Features

- Text cleaning and normalization
- A lightweight custom stemmer (handles common English suffixes: -tion, -ing, -ed, -er, -ly, -s)
- A `TextModel` class that extracts and stores five feature profiles per text
- Model persistence — save and reload extracted features without re-processing the original text
- Similarity scoring and two-way classification between candidate sources

## Background

Originally built as a final project for an introductory computer science course, applying core programming concepts (dictionaries, string processing, object-oriented design) to a natural language processing problem.# text-authorship-classifier
Python text classifier for authorship attribution based on stylometric features
