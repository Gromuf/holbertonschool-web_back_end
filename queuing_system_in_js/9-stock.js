import express from "express";
import redis from "redis";
import { promisify } from "util";

const listProducts = [
  { Id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { Id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { Id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { Id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((item) => item.Id === id);
}

/* Redis */
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

function reserveStockById(itemId, stock) {
  return setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : 0;
}

/* Server */
const app = express();
const port = 1245;

/* GET /list_products */
app.get("/list_products", (req, res) => {
  const products = listProducts.map((item) => ({
    itemId: item.Id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
  }));

  res.json(products);
});

/* GET /list_products/:itemId */
app.get("/list_products/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: "Product not found" });
  }

  const reserved = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.stock - reserved;

  return res.json({
    itemId: item.Id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity,
  });
});

/* GET /reserve_product/:itemId */
app.get("/reserve_product/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: "Product not found" });
  }

  const reserved = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.stock - reserved;

  if (currentQuantity <= 0) {
    return res.json({
      status: "Not enough stock available",
      itemId,
    });
  }

  await reserveStockById(itemId, reserved + 1);

  return res.json({
    status: "Reservation confirmed",
    itemId,
  });
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});
