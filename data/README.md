# Dataset Documentation

## Dataset

**Online Retail**

Source: UCI Machine Learning Repository

## Description

The dataset contains transaction-level records from a UK-based online retail business.

Each row represents a transaction line associated with an invoice, product, quantity, price, date, and customer.

## Data Usage

The raw dataset will be used for customer-level behavioral analysis and customer segmentation.

The original dataset is kept locally under:

```text
data/raw/
```

Processed datasets generated during the project will be stored under:

```text
data/processed/
```

## Important Fields

| Field       | Description                              |
| ----------- | ---------------------------------------- |
| InvoiceNo   | Invoice number identifying a transaction |
| StockCode   | Product/item identifier                  |
| Description | Product description                      |
| Quantity    | Number of items purchased                |
| InvoiceDate | Date and time of the transaction         |
| UnitPrice   | Price per item                           |
| CustomerID  | Customer identifier                      |
| Country     | Customer's country                       |

## Data Availability

The raw dataset is intentionally excluded from Git tracking because of its file size.

To reproduce the project, download the original dataset from the UCI Machine Learning Repository and place the extracted file in:

```text
data/raw/
```

## Data Handling Principle

The original raw dataset will not be modified.

All cleaning, transformation, and feature engineering will be performed through reproducible code, with resulting datasets stored separately under:

```text
data/processed/
```
