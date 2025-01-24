import Breadcrumbs from "../../components/Breadcrumbs"
import useFetch from "../../hooks/useFetch";

const HomePage = () => {
    const { data, loading, error } = useFetch("https://jsonplaceholder.typicode.com/posts");

    // if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error}</p>;
    return <><Breadcrumbs /> <div>
      <h1>Posts</h1>
      <ul>
        {data.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div></>
}

export default HomePage