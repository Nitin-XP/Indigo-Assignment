import axios from "axios";
import React, { useEffect, useState } from 'react';
// import { flightData } from "../data/data";

const Home = () => {
    const [flightData, setFlightData] = useState([{}]);
    const checkStatus = (status) => {
        if (status === "Delayed") {
            return "text-red-600";
        }
        else if (status === "Cancelled") {
            return "text-gray-600";
        }
        else {
            return "text-green-600";
        }
    }
    useEffect(() => {
        axios.get('http://localhost:5000/flightData')
            .then(res => {
                setFlightData(res.data);
                console.log(res.data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []);

    return (
        <>
            <div className="homeBg">
                <div className=" items-center align-middle text-center">
                    <h1 className=" font-extrabold text-black text-[30px]">Flight Status: Delays, Cancellations, and Gate Changes</h1>
                </div>

                <div className="overflow-x-auto p-2">
                    <table className="table table-xs" >
                        <thead>
                            <tr bgcolor="black" className=" text-white p-5">
                                <th>Flight ID</th>
                                <th>Airline</th>
                                <th>Status</th>
                                <th>Scheduled Arrival</th>
                                <th>Actual Arrival</th>
                                <th>Arrival Gate</th>
                                <th>Scheduled Departure</th>
                                <th>Actual Departure</th>
                                <th>Departure Gate</th>
                            </tr>
                        </thead>
                        <tbody className=" bg-white">
                            {
                                typeof flightData === 'undefined' ? (<h2>Loading..</h2>) : flightData.map((data, i) => (
                                    <tr key={i} className=" hover:bg-slate-300 text-gre">
                                        <td>{data.flight_id}</td>
                                        <td>{data.airline}</td>
                                        <td className={`${checkStatus(data.status)} font-semibold`}>{data.status}</td>
                                        <td>{data.scheduled_arrival}</td>
                                        <td>{data.actual_arrival}</td>
                                        <td>{data.arrival_gate}</td>
                                        <td>{data.scheduled_departure}</td>
                                        <td>{data.actual_departure}</td>
                                        <td>{data.departure_gate}</td>
                                    </tr>
                                ))
                            }
                        </tbody>
                    </table>
                </div>
            </div>
        </>
    )
}

export default Home