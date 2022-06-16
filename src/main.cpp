#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "turning-function.h"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

int vec_to_poly(std::vector<std::vector<float>>& points, POLY poly)
{
    static int line = 0;

    if (points.size() < 3) {
        fprintf(stderr, "line %d: null polygon\n", line);
        exit(1);
    }

    if (points.size() > MAX_PTS) {
        fprintf(stderr, "line %d: polygon too big\n", line);
        exit(1);
    }

    int i = 0;
    for (auto pair : points) {
        poly->pt[i].x = pair.at(0);
        poly->pt[i].y = pair.at(1);
        i++;
    }

    return(poly->n = points.size());
}

double turningFunctionMetric(std::vector<std::vector<float>> points1, std::vector<std::vector<float>> points2) {

    TURN_REP_REC trf, trg;
    TURN_REP f, g;
    POLY_REC pf, pg;
    EVENT_REC e;

    double ht0, slope, alpha, theta_star, metric2, metric, ht0_err, slope_err;

    // todo: should update_p be 1 or 0
    int update_p = 0;
    int precise_p = 1;

    if ((points1.size() < 3 || points1.size() > MAX_PTS) ||
        points2.size() < 3 || points2.size() > MAX_PTS) {
        throw std::runtime_error("List of points is a bad size.");
    }

    vec_to_poly(points1, &pf);
    vec_to_poly(points2, &pg);

    poly_to_turn_rep(&pf, &trf);
    f = &trf;

    poly_to_turn_rep(&pg, &trg);
    g = &trg;

    init_vals(f, g, &ht0, &slope, &alpha);
    init_events(f, g);

    metric2 = h_t0min(f, g, 
        ht0, slope, alpha,
        update_p ? reinit_interval(f, g) : 0,
        &theta_star, &e, &ht0_err, &slope_err);

    /*
     * Fixups: The value of metric2 can be a tiny
     * negative number for an exact match.  Call it 0.
     * Theta_star can be over 360 or under -360 because we
     * handle t=0 events at t=1. Normalize to [-PI,PI).
     */
    metric = metric2 > 0 ? sqrt(metric2) : 0;
    // printf(precise_p ? "%.18lg %.18lg %d %d %lg %lg" : "%lg %lg %d %d %lg %lg",
    //        metric, turn(theta_star, 0)*180/M_PI,
    //        tr_i(f, e.fi), tr_i(g, e.gi), ht0_err, slope_err);

    return metric;
}

namespace py = pybind11;

PYBIND11_MODULE(turning_function, m) {
    m.doc() = R"pbdoc(
        Turning Function python module
        -----------------------

        .. currentmodule:: turning_function

        .. autosummary::
           :toctree: _generate

           distance
    )pbdoc";

    m.def("distance", &turningFunctionMetric, py::arg("points_a"), py::arg("points_b"), R"pbdoc(
        Compute the turning function metric for two lists of points.

        Each argument should be a list of points shaped Nx2.
    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}