

using TaskManagementAPI.DTOs;
using TaskManagementAPI.Models;

namespace TaskManagementAPI.Services
{
    public interface ITaskServices
    {
        List<TaskItem> GetAll();
        TaskItem? GetById(int id);
        TaskItem Create(TaskItemDTO dto);
        bool Delete(int id);
    }
}