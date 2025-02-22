import React from "react";
import Breadcrumbs from "../../components/Breadcrumbs";
import useFetch from "../../hooks/useFetch";

const ServicePage = () => {
    const { data, loading, error } = useFetch("https://jsonplaceholder.typicode.com/posts/1");

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error}</p>;

    return (
        <>
            <Breadcrumbs />
            <div>
                <h1>Post</h1>
                <p>{data?.title}</p>
            </div>
        </>
    );
};

export default ServicePage;
