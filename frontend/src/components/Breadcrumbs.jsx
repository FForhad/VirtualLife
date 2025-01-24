import React from "react";
import { Link, useLocation } from "react-router-dom";

const Breadcrumbs = () => {
  const location = useLocation();
  const pathnames = location.pathname.split("/").filter((x) => x);
console.log(pathnames);

  return (
    <nav aria-label="breadcrumb" className="breadcrumbs">
      <ol>
        <li>
          <Link to="/">Home</Link>
        </li>
        {pathnames.map((value, index) => {
          const to = `/${pathnames.slice(0, index + 1).join("/")}`;
          const isLast = index === pathnames.length - 1;

          return (
            <li key={to} aria-current={isLast ? "page" : undefined}>
              {isLast ? (
                <span>{value}</span>
              ) : (
                <Link to={to}>{value.replace("-", " ")}</Link>
              )}
            </li>
          );
        })}
      </ol>
    </nav>
  );
};

export default Breadcrumbs;
