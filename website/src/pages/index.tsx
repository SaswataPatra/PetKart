import Collection from "@/components/Collection";
import Hero from "@/components/Hero";
import { fetchProducts } from "@/lib/api";
import { useEffect, useState } from "react";

export default function IndexPage() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetchProducts().then(setProducts);
  }, []);

  return (
    <>
      <Hero />
      <div id="products">
        <Collection products={products} />
      </div>
    </>
  );
}
